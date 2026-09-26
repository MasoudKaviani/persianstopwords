# Persian (Farsi) Stopwords

A comprehensive, curated list of Persian (Farsi) stopwords for text processing, NLP, search indexing, and corpus cleaning.

## Overview

This dataset aggregates Persian stopwords from multiple open-source repositories and linguistic resources, then refines them through deduplication, cleaning, and alphabetical sorting. It contains over **2,900 stopwords** including:

- **Pronouns & demonstratives** — آن، این، او، آنها، خود، etc.
- **Prepositions & postpositions** — از، به، در، با، برای, etc.
- **Conjunctions** — و، یا، اما، که، چون, etc.
- **Verbs & verb forms** — است، بود، شد، می‌کند, etc.
- **Adverbs** — خیلی، بسیار، فقط، همیشه, etc.
- **Question words** — چه، کی، کجا، چرا, etc.
- **Filler & interjection words** — خب، آها، آهان, etc.
- **Punctuation marks** — Persian and common punctuation

## Usage

### Python

```python
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = set(line.strip() for line in f if line.strip())

text = "این یک متن نمونه برای پاک‌سازی است"
cleaned = [word for word in text.split() if word not in stopwords]
print(' '.join(cleaned))
```

### Node.js

```javascript
const fs = require('fs');

const stopwords = new Set(
  fs.readFileSync('stopwords.txt', 'utf-8')
    .split('\n')
    .map(w => w.trim())
    .filter(Boolean)
);

const text = "این یک متن نمونه برای پاک‌سازی است";
const cleaned = text.split(' ').filter(w => !stopwords.has(w));
console.log(cleaned.join(' '));
```

### NLTK

```python
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    my_stopwords = [line.strip() for line in f]

from nltk.corpus import stopwords as nltk_stopwords
nltk_stopwords.words('persian')  # NLTK also uses a similar list
```

## File Structure

```
.
├── stopwords.txt    # The main stopwords list (one word per line, UTF-8)
├── resources.txt    # List of source repositories and references
├── LICENSE           # MIT License
└── README.md         # This file
```

## Format

- **Encoding:** UTF-8
- **Format:** One word per line
- **Sorting:** Persian alphabetical order (آ ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی)
- **Normalization:** Zero-width characters and BOM removed; duplicates removed

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
2. Edit `stopwords.txt` (keep alphabetical order and one word per line)
3. Submit a pull request

Please ensure entries are:
- Genuinely stopwords (high-frequency words that carry little semantic meaning)
- In standard Persian script (avoid ASCII-only or garbled entries)
- Not duplicates of existing entries

## License

[MIT License](LICENSE) — Copyright (c) 2022 Masoud Kaviani

---

# دیتاست مجموعه کلمات توقف فارسی

این مجموعه داده، شامل بیش از **۲,۹۰۰ کلمه توقف فارسی** است که از منابع مختلف جمع‌آوری، پاک‌سازی، و مرتب‌سازی شده است. می‌توانید برای پاک‌سازی متون، پردازش زبان طبیعی، فهرست‌سازی جستجو و کاربردهای مشابه از آن استفاده کنید.

## نحوه استفاده

فایل `stopwords.txt` را باز کرده و کلمات توقف را به صورت مجموعه‌ای از کلمات بارگذاری کنید:

```python
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = set(line.strip() for line in f if line.strip())
```

## منابع

منابع این مجموعه داده در فایل [`resources.txt`](resources.txt) listing شده‌اند.
