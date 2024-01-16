"""
Functions specifically related to cleaning punctuation characters (as classified in
Wikipedia; https://en.wikipedia.org/wiki/Japanese_punctuation)
"""

from jp_broom.mapping.patterns import *


def clean_brackets(text: str, remove=False) -> str:
    """Standardizes brackets to the standard left and right brackets.

    Args:
        text: Input text
        remove: If True, remove brackets instead of standardizing them

    Returns:
        Text with brackets standardized to the standard left and right brackets.
    """
    if remove:
        text = LEFT_BRACKET_PATTERN.sub("", text)
        text = RIGHT_BRACKET_PATTERN.sub("", text)
    else:
        text = LEFT_BRACKET_PATTERN.sub(STANDARD_LEFT_BRACKET, text)
        text = RIGHT_BRACKET_PATTERN.sub(STANDARD_RIGHT_BRACKET, text)
    return text


def clean_commas(text: str, remove=False, convert=False) -> str:
    """Standardizes commas to the standard comma.

    Args:
        text: Input text
        remove: If True, remove commas instead of standardizing them
        convert: If True, convert all commas to a space

    Returns:
        Text with commas standardized to the standard comma.
    """
    if remove:
        text = COMMA_PATTERN.sub("", text)
    elif convert:
        text = COMMA_PATTERN.sub(" ", text)
    else:
        text = COMMA_PATTERN.sub(STANDARD_COMMA, text)
    return text


def clean_double_hyphens(text: str, remove=False) -> str:
    """Standardizes double hyphens to the standard double hyphen.

    Args:
        text: Input text
        remove: If True, remove double hyphens instead of standardizing them

    Returns:
        Text with double hyphens standardized to the standard double hyphen.
    """
    if remove:
        text = DOUBLE_HYPHEN_PATTERN.sub("", text)
    else:
        text = DOUBLE_HYPHEN_PATTERN.sub(STANDARD_DOUBLE_HYPHEN, text)
    return text


def clean_ellipses(text: str, remove=False) -> str:
    """Standardizes ellipses to the standard ellipsis.

    Args:
        text: Input text
        remove: If True, remove ellipses instead of standardizing them

    Returns:
        Text with ellipses standardized to the standard ellipsis.
    """
    if remove:
        text = ELLIPSIS_PATTERN.sub("", text)
    else:
        text = ELLIPSIS_PATTERN.sub(STANDARD_ELLIPSIS, text)
    return text


def clean_full_stops(text: str, remove=False, convert=False) -> str:
    """Standardizes full stops to the standard full stop.

    Args:
        text: Input text
        remove: If True, remove full stops instead of standardizing them
        convert: If True, convert all full stops to a space

    Returns:
        Text with full stops standardized to the standard full stop.
    """
    if remove:
        text = FULL_STOP_PATTERN.sub("", text)
    elif convert:
        text = FULL_STOP_PATTERN.sub(" ", text)
    else:
        text = FULL_STOP_PATTERN.sub(STANDARD_FULL_STOP, text)
    return text


def clean_wave_dash(text: str, remove=False) -> str:
    """Standardizes wave dashes to the standard wave dash.

    Args:
        text: Input text
        remove: If True, remove wave dashes instead of standardizing them

    Returns:
        Text with wave dashes standardized to the standard wave dash.
    """
    if remove:
        text = WAVE_DASH_PATTERN.sub("", text)
    else:
        text = WAVE_DASH_PATTERN.sub(STANDARD_WAVE_DASH, text)
    return text
