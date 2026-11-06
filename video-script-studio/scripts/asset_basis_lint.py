#!/usr/bin/env python3
"""Literal checks for asset design-basis records (references/asset-design-basis.md).

Checks, per C/B/P/S asset in asset-registry.json:
  - a design_basis record exists, with the required keys for its type;
  - every design_basis item has non-empty text and a source (a citation,
    "推导", or "不适用：<reason>");
  - every script_features entry has feature/scene/where, and where is
    base | video | state:<name> with <name> present in state_plan;
  - features marked base/state appear literally in the asset's prompt block
    (base) or are planned in state_plan (state);
  - the asset's prompt block carries no external film/series style anchor.

It does not judge whether a derivation is right or whether an image fits the
story. Exit 0 = no FAIL; 1 = FAIL; 2 = input error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = {
    'C': ('world', 'identity', 'traces', 'origin', 'personality'),
    'B': ('world', 'identity', 'traces'),
    'P': ('world', 'identity', 'traces', 'origin'),
    'S': ('world', 'identity', 'traces', 'origin'),
}
NAME_ANCHOR = re.compile(r'《[^》]{1,40}》[^，。,\n]{0,24}(质感|风格|画风|色调|影像|摄影|美术|感)')
EN_ANCHOR = re.compile(r'\b(in the style of|inspired by|à la)\b', re.I)


def asset_type(asset: dict) -> str | None:
    kind = asset.get('type') or asset.get('category')
    if isinstance(kind, str) and kind[:1].upper() in REQUIRED:
        return kind[:1].upper()
    return None


def prompt_block(text: str, asset: dict) -> str | None:
    """Return the prompt section for this asset: from its heading to the next heading."""
    handle = asset.get('handle', '')
    name = asset.get('name', '')
    heads = [m for m in re.finditer(r'(?m)^#{1,3} .*$', text)]
    for i, m in enumerate(heads):
        line = m.group(0)
        if (handle and handle in line) or (name and f'{name}@' in line):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            return text[m.start():end]
    return None


def check(registry: dict, root: Path) -> list[tuple[str, str, str]]:
    findings = []
    for asset in registry.get('assets', []):
        kind = asset_type(asset)
        if kind is None:
            continue
        label = asset.get('handle') or asset.get('name') or '?'
        basis = asset.get('design_basis')
        if not isinstance(basis, dict):
            findings.append(('FAIL', label, 'missing design_basis'))
            continue
        for key in REQUIRED[kind]:
            item = basis.get(key)
            if not isinstance(item, dict) or not str(item.get('text', '')).strip():
                findings.append(('FAIL', label, f'design_basis.{key}: missing text'))
                continue
            source = str(item.get('source', '')).strip()
            if not source:
                findings.append(('FAIL', label, f'design_basis.{key}: missing source'))
            elif source.startswith('不适用') and not re.match(r'不适用[：:]\s*\S', source):
                findings.append(('FAIL', label, f'design_basis.{key}: 不适用 needs a reason'))
            elif source == '推导':
                findings.append(('WARN', label, f'design_basis.{key}: derived, confirm with user'))

        states = {s.get('state') for s in asset.get('state_plan', []) if isinstance(s, dict)}
        text = None
        if asset.get('prompt_file'):
            path = root / asset['prompt_file']
            if path.is_file():
                text = prompt_block(path.read_text(encoding='utf-8'), asset)
                if text is None:
                    findings.append(('FAIL', label, f'prompt block not found in {asset["prompt_file"]}'))
            else:
                findings.append(('FAIL', label, f'prompt_file not found: {asset["prompt_file"]}'))
        else:
            findings.append(('WARN', label, 'no prompt_file; base features not checked'))

        for feat in asset.get('script_features', []):
            if not isinstance(feat, dict) or not all(feat.get(k) for k in ('feature', 'scene', 'where')):
                findings.append(('FAIL', label, f'script_features entry incomplete: {feat}'))
                continue
            where = feat['where']
            if where == 'base':
                if text is not None and feat['feature'] not in text:
                    findings.append(('FAIL', label, f'feature "{feat["feature"]}" ({feat["scene"]}) not in prompt'))
            elif where.startswith('state:'):
                if where[6:] not in states:
                    findings.append(('FAIL', label, f'feature "{feat["feature"]}" points to unplanned {where}'))
            elif where != 'video':
                findings.append(('FAIL', label, f'feature "{feat["feature"]}": unknown where {where!r}'))

        if text is not None:
            body = '\n'.join(block for block in re.findall(r'```(?:text)?\n(.*?)```', text, re.S)) or text
            hit = NAME_ANCHOR.search(body) or EN_ANCHOR.search(body)
            if hit:
                findings.append(('FAIL', label, f'external style anchor in prompt: "{hit.group(0)}"'))
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--asset-registry', required=True, type=Path)
    parser.add_argument('--project-root', type=Path,
                        help='base for prompt_file paths (default: registry folder)')
    args = parser.parse_args(argv)
    try:
        registry = json.loads(args.asset_registry.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'ERROR: cannot read registry: {exc}', file=sys.stderr)
        return 2
    root = args.project_root or args.asset_registry.parent
    findings = check(registry, root)
    for severity, label, message in findings:
        print(f'{severity}: {label}: {message}')
    fails = sum(1 for f in findings if f[0] == 'FAIL')
    print(f'{"FAIL" if fails else "PASS"}: {fails} FAIL, {len(findings) - fails} WARN; '
          'literal checks only, derivation quality and image fit not judged.')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
