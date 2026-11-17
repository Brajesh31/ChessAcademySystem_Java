#!/usr/bin/env python3
"""Validate required documentation files and local Markdown links."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md", "LICENSE",
    "docs/README.md", "docs/architecture.md", "docs/testing.md",
    "docs/security.md", "docs/data-formats.md", "docs/templates/README.md",
]
missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
errors = [f"Missing required file: {name}" for name in missing]

# Markdown links and image links. Ignore remote URLs and fragment-only links.
link_pattern = re.compile(r"!?(\[[^\]]*\])\(([^)]+)\)")
for md in ROOT.rglob("*.md"):
    if any(part.startswith(".") for part in md.relative_to(ROOT).parts):
        continue
    text = md.read_text(encoding="utf-8")
    for _, target in link_pattern.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{md.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{md.relative_to(ROOT)}: broken local link: {target}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Documentation validation passed. Checked {len(REQUIRED)} required files and local Markdown links.")
