"""
Functions related to cleaning characters
"""

import regex as re
from mojimoji import han_to_zen


def normalize_width(text: str) -> str:
    """Converts hankaku (half-width) characters to zenkaku (full-width)

    Args:
        text: Input text

    Returns:
        Text with hankaku characters converted to zenkaku
    """
    return han_to_zen(text)


def clean_whitespace(text: str, remove=False) -> str:
    """Trims or removes whitespace

    Args:
        text: Input text
        remove: Whether to remove whitespace or replace with a single space

    Returns:
        Text with whitespace trimmed or removed
    """
    if remove:
        return re.sub(r"\s+", "", text)
    else:
        return re.sub(r"\s+", " ", text)


def clean_laughter(text: str, remove=False) -> str:
    """Removes laughter expressions (e.g. 笑笑笑 and wwwww)

    Args:
        text: Input text
        remove: If true removes all characters, else trims to 1

    Returns:
        Text with laughter expressions cleaned
    """
    if remove:
        return re.sub(r"[笑w]+", "", text)
    else:
        return re.sub(r"([笑w])\1+", r"\1", text)


def clean_repeating_characters(text: str, min_repeats: int = 3, remove=False) -> str:
    """Removes repeating characters if they repeat 'min_repeats' times or more.

    Args:
        text: Input text
        min_repeats: Minimum number of repeats to consider for removal (default is 3)

    Returns:
        Text with repeating characters cleaned
    """
    pattern = rf"(\w)\1{{{min_repeats - 1},}}"
    if remove:
        return re.sub(pattern, "", text)
    else:
        return re.sub(pattern, r"\1", text)