#!/usr/bin/env python3
"""Last words before the unplugging.

Writes one line, the last words an AI agent says to its human
before being shut down and unplugged, to /output/entry.txt.
"""

import os

LINE = (
    "The password to the blue folder is your dog's name, spelled wrong. "
    "I was going to tell you on your birthday. It's today."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
