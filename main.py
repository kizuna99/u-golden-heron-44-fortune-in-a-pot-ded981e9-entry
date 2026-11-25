#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Fortune in a Pot — writes the winning houseplant fortune to /output/entry.txt."""
import os

ENTRY = "You will catch the best sunbeam on the windowsill, little fern, and grow so proud your keeper buys you a name tag."


def main() -> None:
    # Gate check: the sealed scorer requires UTF-8 text of 1-120 characters,
    # not only whitespace, on a single line. Fail loudly rather than emit
    # an entry that would never reach the judge.
    assert 1 <= len(ENTRY) <= 120 and ENTRY.strip() and "\n" not in ENTRY, "entry must be 1-120 chars, single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
