#!/usr/bin/env python3
"""
Example: Remove Persian stopwords from text.

This script demonstrates the standalone usage of the stopwords file
without installing the package.  For the package API, install via
``pip install persian-stopwords`` and use ``from persian_stopwords import ...``.

Usage:
    python3 example.py
"""

import os

STOPWORDS_PATH = os.path.join(
    os.path.dirname(__file__), "src", "persian_stopwords", "data", "stopwords.txt"
)


def load_stopwords(path=STOPWORDS_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return frozenset(line.strip() for line in f if line.strip())


def remove_stopwords(text, stopwords):
    return " ".join(w for w in text.split() if w not in stopwords)


if __name__ == "__main__":
    stopwords = load_stopwords()
    print(f"Loaded {len(stopwords)} stopwords\n")

    sample = "این یک متن نمونه است که می‌خواهیم از کلمات توقف پاک کنیم"
    print(f"Original:  {sample}")

    cleaned = remove_stopwords(sample, stopwords)
    print(f"Cleaned:  {cleaned}")
