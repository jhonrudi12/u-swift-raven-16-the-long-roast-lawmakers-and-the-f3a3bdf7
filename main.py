#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) roasting lawmakers
who would regulate AI, crypto or the internet but cannot convert a file to
PDF. The sentence is embedded below and written verbatim to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output``).

Python 3 standard library only. Deterministic, no network, no randomness.
"""

import os
import sys

SENTENCE = (
    "The committee deciding what your AI may say spent the morning debating "
    "whether renaming a file from .docx to .pdf counts as converting it."
)

MAX_CHARS = 320


def main() -> int:
    sentence = SENTENCE.strip()
    if not sentence:
        print("error: sentence is empty", file=sys.stderr)
        return 1
    if "\n" in sentence or "\r" in sentence:
        print("error: sentence must be a single line", file=sys.stderr)
        return 1
    if len(sentence) > MAX_CHARS:
        print(
            "error: sentence is %d characters, over the %d limit"
            % (len(sentence), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(sentence)
    # Verify what landed on disk is exactly the sentence we validated.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != sentence:
        print("error: written output does not match the sentence", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
