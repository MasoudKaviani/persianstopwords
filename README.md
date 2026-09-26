# Persian (Farsi) Stopwords

[![PyPI version](https://badge.fury.io/py/persian-stopwords.svg)](https://pypi.org/project/persian-stopwords/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A comprehensive, curated list of Persian (Farsi) stopwords for text processing, NLP, search indexing, and corpus cleaning.

## Installation

```bash
pip install persian-stopwords
```

## Quick Start

```python
from persian_stopwords import load_stopwords, clean_text

# Load the stopwords set
stopwords = load_stopwords()
print(f"{len(stopwords)} stopwords loaded")

# Remove stopwords from text
cleaned = clean_text("این یک متن نمونه است که می‌خواهیم پاک کنیم")
print(cleaned)
# Output: متن نمونه می‌خواهیم پاک
```

## API

### `load_stopwords() -> frozenset[str]`

Returns the full set of Persian stopwords as a frozenset. Data is loaded from package resources, so it works from any working directory.

```python
from persian_stopwords import load_stopwords

stopwords = load_stopwords()
```

### `remove_stopwords(tokens, stopwords=None) -> list[str]`

Filters stopwords out of an iterable of tokens. If `stopwords` is `None`, uses the built-in list.

```python
from persian_stopwords import remove_stopwords

tokens = "این یک متن نمونه است".split()
cleaned = remove_stopwords(tokens)
```

### `clean_text(text, stopwords=None) -> str`

Removes Persian stopwords from a whitespace-delimited string.

```python
from persian_stopwords import clean_text

result = clean_text("این یک متن نمونه است")
```

## What's Included

Over **2,900 stopwords** including:

- **Pronouns & demonstratives** — آن، این، او، آنها، خود، etc.
- **Prepositions & postpositions** — از، به، در، با، برای, etc.
- **Conjunctions** — و، یا، اما، که، چون, etc.
- **Verbs & verb forms** — است، بود، شد، می‌کند, etc.
- **Adverbs** — خیلی، بسیار، فقط، همیشه, etc.
- **Question words** — چه، کی، کجا، چرا, etc.
- **Filler & interjection words** — خب، آها، آهان, etc.
- **Punctuation marks** — Persian and common punctuation

## Data Format

- **Encoding:** UTF-8
- **Format:** One word per line
- **Sorting:** Persian alphabetical order (آ ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی)
- **Normalization:** Zero-width characters and BOM removed; duplicates removed

## File Structure

```
.
├── pyproject.toml                    # Build config and package metadata
├── MANIFEST.in                       # Include data files in sdist
├── README.md
├── LICENSE
├── resources.txt                     # List of source references
├── example.py                        # Standalone usage example
└── src/
    └── persian_stopwords/
        ├── __init__.py               # Package API
        └── data/
            └── stopwords.txt         # The stopwords list (UTF-8)
```

## Sources

This dataset aggregates and refines stopwords from the following sources (see [`resources.txt`](resources.txt) for full links):

- [larsyencken/1440509](https://gist.github.com/larsyencken/1440509) — Multilingual stopwords gist
- [ziaa/Persian-stopwords-collection](https://github.com/ziaa/Persian-stopwords-collection) — Collection of Persian stopword lists
- [kharazi/persian-stopwords](https://github.com/kharazi/persian-stopwords) — Persian stopwords repository
- [ranks.nl Persian stopwords](https://www.ranks.nl/stopwords/persian) — Online stopword resource
- [amirshnll/persian-stop-word](https://github.com/amirshnll/persian-stop-word) — Persian stop words list
- [aftab.cc](https://aftab.cc/article/1232) — Article on Persian stop words

## Contributing

Contributions are welcome! If you find missing stopwords or entries that should be removed:

1. Fork this repository
2. Edit `src/persian_stopwords/data/stopwords.txt` (keep alphabetical order and one word per line)
3. Submit a pull request

Please ensure entries are:
- Genuinely stopwords (high-frequency words that carry little semantic meaning)
- In standard Persian script (avoid ASCII-only or garbled entries)
- Not duplicates of existing entries

## Publishing (for maintainers)

```bash
# Build the package
python -m build

# Upload to PyPI
twine upload dist/*
```

## License

[MIT License](LICENSE) — Copyright (c) 2022 Masoud Kaviani

---

# دیتاست مجموعه کلمات توقف فارسی

این مجموعه داده، شامل بیش از **۲,۹۰۰ کلمه توقف فارسی** است که از منابع مختلف جمع‌آوری، پاک‌سازی، و مرتب‌سازی شده است. می‌توانید برای پاک‌سازی متون، پردازش زبان طبیعی، فهرست‌سازی جستجو و کاربردهای مشابه از آن استفاده کنید.

## نصب

```bash
pip install persian-stopwords
```

## استفاده

```python
from persian_stopwords import load_stopwords, clean_text

stopwords = load_stopwords()
cleaned = clean_text("این یک متن نمونه است")
```

## منابع

منابع این مجموعه داده در فایل [`resources.txt`](resources.txt) listing شده‌اند.
