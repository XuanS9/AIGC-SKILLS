#!/usr/bin/env python3
"""Offline structural checks for script-writing-studio.

This checks local packaging and routing references only. It does not evaluate
story quality, model behavior, generation results, or market performance.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []

entry = ROOT / "SKILL.md"
if not entry.is_file():
    errors.append("missing root SKILL.md")
else:
    text = entry.read_text(encoding="utf-8")
    if not re.search(r"^---\s*\n.*?^name:\s*script-writing-studio\s*$", text, re.M | re.S):
        errors.append("SKILL.md frontmatter name is missing or incorrect")
    if not re.search(r"^description:\s*\S", text, re.M):
        errors.append("SKILL.md description is missing")

md_files = list(ROOT.rglob("*.md"))
for path in md_files:
    text = path.read_text(encoding="utf-8")
    prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
    for raw in re.findall(r"!?\[[^\]\n]*\]\(([^\n)]+)\)", prose):
        target = raw.strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
        if not target or target.startswith("#") or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not target:
            continue
        dest = (path.parent / target).resolve()
        if not dest.is_relative_to(ROOT.resolve()):
            errors.append(f"{path.relative_to(ROOT)}: link leaves Skill: {raw}")
        elif not dest.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing local link: {raw}")

# Explicit Skill routing must use names, not broken relative paths.
all_text = "\n".join(p.read_text(encoding="utf-8") for p in md_files)
for bad in ("../script-package-production/SKILL.md", "../../script-package-production/SKILL.md",
            "../canvas-production/SKILL.md", "../../canvas-production/SKILL.md"):
    if bad in all_text:
        errors.append(f"stale cross-Skill relative route: {bad}")

# There must be exactly one active entry in this package.
entries = [p for p in ROOT.rglob("SKILL.md") if p.is_file()]
if entries != [entry]:
    errors.append("expected exactly one active SKILL.md entry")

print(f"checked {len(md_files)} markdown files and {len(entries)} active entry")
if errors:
    print("FAIL")
    print("\n".join(errors))
    sys.exit(1)
print("PASS: local links, entry, and Skill routing checks passed")
