from jp_broom.mapping.punctuation import *


def standardize_brackets(text: str) -> str:
    """Standardizes brackets to the standard left and right brackets.

    Args:
        text: Input text

    Returns:
        Text with brackets standardized to the standard left and right brackets.
    """
    text = LEFT_BRACKET_PATTERN.sub(STANDARD_LEFT_BRACKET, text)
    text = RIGHT_BRACKET_PATTERN.sub(STANDARD_RIGHT_BRACKET, text)
    return text


def standardize_commas(text: str) -> str:
    """Standardizes commas to the standard comma.

    Args:
        text: Input text

    Returns:
        Text with commas standardized to the standard comma.
    """
    text = COMMA_PATTERN.sub(STANDARD_COMMA, text)
    return text


def standardize_double_hyphens(text: str) -> str:
    """Standardizes double hyphens to the standard double hyphen.

    Args:
        text: Input text

    Returns:
        Text with double hyphens standardized to the standard double hyphen.
    """
    text = DOUBLE_HYPHEN_PATTERN.sub(STANDARD_DOUBLE_HYPHEN, text)
    return text


def standardize_ellipses(text: str) -> str:
    """Standardizes ellipses to the standard ellipsis.

    Args:
        text: Input text

    Returns:
        Text with ellipses standardized to the standard ellipsis.
    """
    text = ELLIPSIS_PATTERN.sub(STANDARD_ELLIPSIS, text)
    return text


def standardize_full_stops(text: str) -> str:
    """Standardizes full stops to the standard full stop.

    Args:
        text: Input text

    Returns:
        Text with full stops standardized to the standard full stop.
    """
    text = FULL_STOP_PATTERN.sub(STANDARD_FULL_STOP, text)
    return text