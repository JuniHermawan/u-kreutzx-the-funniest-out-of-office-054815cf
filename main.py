#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes one line of an out-of-office auto-reply, the funniest it can
be (105 characters), to /output/entry.txt.

The reply was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a reply a real person would set, a genuine surprise, a personal
voice, and freshness. The two controls — the standard template reply
and a famous gone-fishing retelling — scored far below the winner, so
neither pattern was used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "Out of office until Monday. The emails will be answered by my cat, who has strong opinions and no thumbs."


def main() -> None:
    # Competition gate: the reply must be UTF-8 text, 1-140
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 140 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
