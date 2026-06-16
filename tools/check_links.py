#!/usr/bin/env python3
"""Verify that internal (relative) Markdown links point to files that exist.

Scans every .md file in the repo, extracts links of the form [text](target),
ignores external (http...) and anchor-only (#...) links, and checks the rest
resolve to a real file. Exits non-zero if any are broken.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ROOT = Path(__file__).resolve().parent.parent


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def main() -> int:
    broken: list[str] = []
    md_files = sorted(ROOT.rglob("*.md"))

    for md in md_files:
        text = md.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.split("#", 1)[0].strip()  # drop anchors
            if not target or is_external(raw):
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{md.relative_to(ROOT)} -> {target}")

    if broken:
        print("Broken internal links found:")
        for b in broken:
            print(f"  ✗ {b}")
        return 1

    print(f"OK — checked {len(md_files)} Markdown files, no broken internal links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
