#!/usr/bin/env python3
"""Cross-platform RULE 2 check: no trade/finance leakage in core/.

This file mirrors the bash rule check without requiring Git Bash on Windows.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CORE = REPO / "core"
FORBIDDEN_PATTERNS = [
    "Bull",
    "Bear",
    "trader",
    "ticker",
    "yfinance",
    "Alpha Vantage",
    "stock",
]
ATTRIBUTION_HINTS = (
    "Adapted from",
    "RULE 2",
    "KHONG",
    "KHÔNG",
    "was:",
)


def _is_allowed_line(line: str) -> bool:
    text = line.strip()
    if not text:
        return True
    if text.startswith("#"):
        return any(hint in text for hint in ATTRIBUTION_HINTS)
    return False


def main() -> int:
    failed = False
    for pattern in FORBIDDEN_PATTERNS:
        print(f"Checking: {pattern}")
        hits: list[str] = []
        for path in sorted(CORE.rglob("*.py")):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = path.read_text(encoding="utf-8", errors="ignore")
            for lineno, line in enumerate(text.splitlines(), start=1):
                if re.search(rf"\b{re.escape(pattern)}\b", line, flags=re.IGNORECASE):
                    if _is_allowed_line(line):
                        continue
                    rel = path.relative_to(REPO)
                    hits.append(f"{rel}:{lineno}:{line.strip()}")
        if hits:
            print(f"❌ Found '{pattern}' in core/ (non-attribution lines):")
            for hit in hits:
                print(f"  {hit}")
            failed = True
        else:
            print("  (ok — no forbidden matches)")
    if failed:
        print("\n❌ Domain-neutral check FAILED")
        return 1
    print("\n✅ Domain-neutral check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
