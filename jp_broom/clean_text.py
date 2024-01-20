"""
This file will contain functions that clean text using the functions found in the helpers sub-directory.
"""
from jp_broom.helpers import (normalize_width, clean_whitespace, clean_laughter,
                              clean_repeating_characters, clean_kaomoji, clean_brackets,
                              clean_commas, clean_numbers,
                              clean_double_hyphens, clean_ellipses, clean_full_stops,
                              clean_wave_dash, clean_sentence_end,
                              clean_misc_characters, tokenize_text)


def clean_light(text: str) -> str:
    """Cleans text using the functions found in the helpers sub-directory.

    Args:
        text: Input text

    Returns:
        Cleaned text
    """
    text = normalize_width(text)
    text = clean_kaomoji(text)
    text = clean_laughter(text, remove=False)
    text = clean_repeating_characters(text, min_repeats=3, remove=False)
    text = clean_brackets(text, remove=False)
    text = clean_commas(text, remove=False, convert=False)
    text = clean_double_hyphens(text, remove=False)
    text = clean_ellipses(text, remove=False)
    text = clean_full_stops(text, remove=False, convert=False)
    text = clean_sentence_end(text, remove=False, convert=False)
    text = clean_wave_dash(text, remove=False)
    text = clean_numbers(text, remove=False, convert=True)
    text = clean_whitespace(text, remove=False, convert=False)
    return text


def clean_deep(text: str) -> str:
    """Cleans text using the functions found in the helpers sub-directory,
    and splits to sentences with a space in them

    Args:
        text: Input text

    Returns:
        Cleaned text
    """
    text = normalize_width(text)
    text = clean_kaomoji(text)
    text = clean_misc_characters(text)
    text = clean_laughter(text, remove=True)
    text = clean_repeating_characters(text, min_repeats=3, remove=True)
    text = clean_brackets(text, remove=True)
    text = clean_commas(text, remove=False, convert=True)
    text = clean_double_hyphens(text, remove=True)
    text = clean_ellipses(text, remove=True)
    text = clean_full_stops(text, remove=False, convert=True)
    text = clean_sentence_end(text, remove=False, convert=True)
    text = clean_wave_dash(text, remove=True)
    text = clean_numbers(text, remove=True, convert=False)
    text = clean_whitespace(text, remove=False, convert=True)
    return text


def clean_deep_tokenize(text: str) -> str:
    """On top of a deep clean, removes stop words, lemmatizes and tokenizes the text.

    Args:
        text: Input text

    Returns:
        Tokenized text
    """
    text = clean_deep(text)
    text, tokens = tokenize_text(text, remove_stop_words=True, lemmatize=True)
    return text, tokens
