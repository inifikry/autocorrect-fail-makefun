#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (under 200 characters) that reads as a hilarious
autocorrect fail to /output/entry.txt. Deterministic, standard library
only: the same line is written on every run.
"""

LINE = (
    "I'd like to book a table for two tonight, please \u2014 "
    "it's our first analversary and I want everything "
    "to be perfect for my wife."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
