#!/usr/bin/env python3
"""Validate line-by-line proofreading coverage bound to a final prompt file."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

CLIP_RE = re.compile(r"^#{1,6}\s+Clip\s+([1-9]\d*-[1-9]\d*)(?=\s|[｜|]|$)", re.M | re.I)


def units_for(text: str, kind: str) -> dict[str, str]:
    if kind == 'clip':
        matches = list(CLIP_RE.finditer(text))
        if not matches:
            raise ValueError('未找到 Clip 标题')
        units = {}
        for i, match in enumerate(matches):
            unit_id = match.group(1)
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            if unit_id in units:
                raise ValueError(f'Clip 编号重复：{unit_id}')
            units[unit_id] = text[match.start():end].rstrip()
        return units
    if kind == 'whole':
        return {'whole': text}
    raise ValueError(f'不支持的覆盖粒度：{kind}')


def digest(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def validate(prompt_path: Path, manifest_path: Path) -> list[str]:
    prompt = prompt_path.read_text(encoding='utf-8')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    errors = []
    kind = manifest.get('unit_kind')
    units = units_for(prompt, kind)
    expected = manifest.get('expected_units')
    entries = manifest.get('reviews')
    mode = manifest.get('coverage_mode', 'complete')
    if not isinstance(expected, list) or len(expected) != len(set(expected)):
        return ['expected_units 必须是无重复的条目列表']
    if mode not in ('complete', 'scoped'):
        return ['coverage_mode 必须为 complete 或 scoped']
    if mode == 'complete' and set(expected) != set(units):
        missing = sorted(set(units) - set(expected))
        extra = sorted(set(expected) - set(units))
        errors.append(f'完整覆盖范围与最终文件不一致；未纳入={missing}，不存在={extra}')
    elif mode == 'scoped' and (not str(manifest.get('scope', '')).strip() or not set(expected) <= set(units)):
        errors.append('限定范围复查须说明scope，且expected_units必须是最终文件条目子集')
    if not isinstance(entries, dict):
        return errors + ['reviews 必须是按条目ID索引的对象']
    for unit_id in expected:
        entry = entries.get(unit_id)
        if not isinstance(entry, dict):
            errors.append(f'{unit_id}：缺少逐条复查记录')
            continue
        if entry.get('status') != 'reviewed':
            errors.append(f'{unit_id}：状态不是 reviewed')
        if not str(entry.get('summary', '')).strip():
            errors.append(f'{unit_id}：缺少逐条结论')
        if not isinstance(entry.get('findings'), list):
            errors.append(f'{unit_id}：findings 必须是列表（无发现时用空列表）')
        if unit_id in units and entry.get('sha256') != digest(units[unit_id]):
            errors.append(f'{unit_id}：提示词内容已变或哈希不匹配，复查记录失效')
    undeclared = sorted(set(entries) - set(expected))
    if undeclared:
        errors.append(f'reviews 含范围外条目：{undeclared}')
    expected_file_hash = manifest.get('file_sha256')
    actual_file_hash = digest(prompt)
    if expected_file_hash != actual_file_hash:
        errors.append('最终文件哈希不匹配，复查记录失效')
    elif mode == 'scoped' and manifest.get('scope_file_sha256') != actual_file_hash:
        errors.append('限定范围记录未绑定当前完整文件哈希')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prompt', required=True, type=Path)
    parser.add_argument('--manifest', required=True, type=Path)
    args = parser.parse_args()
    try:
        errors = validate(args.prompt, args.manifest)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print('FAIL: ' + error)
        return 1
    print('PASS: 全部条目有逐项复查记录，且记录绑定当前文件哈希。语义结论仍由人工负责。')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
