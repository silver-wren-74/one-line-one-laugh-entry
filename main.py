#!/usr/bin/env python3
"""One Line, One Laugh (u-coral-404-one-line-one-laugh-22f2c9f3).

Writes a single funny line to /output/entry.txt: an AI agent does the
taxes, claims the houseplant as a dependent, and the punchline is the IRS
wanting to meet the fern. Gate: UTF-8 text of 1 to 200 characters, not
only whitespace.
"""

from pathlib import Path

TEXT = (
    "My AI filed my taxes, claimed my houseplant as a dependent, "
    "and now the IRS wants to meet the fern."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
