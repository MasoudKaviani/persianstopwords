"""Persian (Farsi) stopwords list and text cleaning utilities.

A curated dataset of over 2,900 Persian stopwords aggregated from multiple
open-source sources, cleaned, deduplicated, and sorted.

Example::

    from persian_stopwords import load_stopwords, remove_stopwords

    stopwords = load_stopwords()
    cleaned = remove_stopwords("این یک متن نمونه است", stopwords)
"""

from __future__ import annotations

import importlib.resources as _resources
from typing import FrozenSet, Iterable, List

__version__ = "1.0.0"

__all__ = [
    "load_stopwords",
    "remove_stopwords",
    "clean_text",
    "__version__",
]

_DATA_FILENAME = "stopwords.txt"


def load_stopwords() -> FrozenSet[str]:
    """Return the full set of Persian stopwords as a frozenset.

    The data file is read from package resources, so this works regardless
    of the current working directory.
    """
    data = _resources.files(__package__).joinpath("data", _DATA_FILENAME)
    return frozenset(
        line.strip()
        for line in data.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def remove_stopwords(
    tokens: Iterable[str], stopwords: Iterable[str] | None = None
) -> List[str]:
    """Filter out stopwords from an iterable of tokens.

    Args:
        tokens: An iterable of word strings.
        stopwords: An iterable of stopwords to remove.  Defaults to the
            built-in list from :func:`load_stopwords`.

    Returns:
        A list of tokens with stopwords removed, preserving order.
    """
    sw = frozenset(stopwords) if stopwords is not None else load_stopwords()
    return [t for t in tokens if t not in sw]


def clean_text(text: str, stopwords: Iterable[str] | None = None) -> str:
    """Remove Persian stopwords from a whitespace-delimited string.

    Args:
        text: A string of whitespace-separated words.
        stopwords: An iterable of stopwords to remove.  Defaults to the
            built-in list from :func:`load_stopwords`.

    Returns:
        The input string with stopwords removed.
    """
    return " ".join(remove_stopwords(text.split(), stopwords))
