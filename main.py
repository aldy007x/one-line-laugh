"""One-Line Laugh entry for make.fun.

Writes a single funny sentence to /output/entry.txt, where the house
judge reads it. The line must be one sentence of at most 200 characters.
"""

import os

LINE = "I put my phone on Do Not Disturb and immediately started disturbing myself."


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, one sentence, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 limit")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry line must be exactly one sentence")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
