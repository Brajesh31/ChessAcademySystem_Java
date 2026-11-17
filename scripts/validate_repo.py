#!/usr/bin/env python3
"""Check expected repository hygiene and project-specific files."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "chessAcademy.java",
    "README.md",
    "LICENSE",
    ".gitignore",
    ".editorconfig",
    ".gitattributes",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/ci.yml",
    ".github/workflows/codeql.yml",
    "docs/assets/project-banner.svg",
    "docs/assets/architecture.svg",
    "docs/assets/application-workflow.svg",
    "docs/templates/feature-specification.md",
    "docs/templates/technical-design.md",
    "docs/templates/test-plan.md",
]
missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
if missing:
    print("Missing repository files:")
    print("\n".join(f"- {p}" for p in missing))
    sys.exit(1)

source = (ROOT / "chessAcademy.java").read_text(encoding="utf-8")
if "class chessAcademy" not in source:
    print("Expected Java class declaration was not found.")
    sys.exit(1)

# Runtime data should never be checked in as project fixtures.
for name in ("data.txt", "tournaments.txt"):
    if (ROOT / name).exists():
        print(f"Warning: {name} exists in the checkout. Confirm it contains no real personal data.")

print(f"Repository validation passed. Checked {len(REQUIRED)} required paths.")
