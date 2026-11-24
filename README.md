# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/jhonrudi12/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/jhonrudi12/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

One satirical sentence (138 characters) roasting lawmakers who would regulate AI, crypto or the internet but cannot convert a file to PDF:

> The committee deciding what your AI may say spent the morning debating whether renaming a file from .docx to .pdf counts as converting it.

The joke turns on the gap between the committee's authority — deciding what your AI may say — and its competence: it cannot tell renaming a file from converting it. The punch lands on the last few words, and the detail (renaming `.docx` to `.pdf`) is the exact, specific failure instead of a worn tech-illiteracy cliché.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes the sentence to `out/entry.txt`. Python 3 standard library only, deterministic, no network. `main.py` validates the sentence (one line, 1–320 characters, not whitespace-only) and verifies the written file matches it byte for byte.
