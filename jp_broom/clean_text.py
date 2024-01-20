"""
This file will contain functions that clean text using the functions found in the helpers sub-directory.
"""
from jp_broom.helpers import (normalize_width, clean_whitespace, clean_laughter,
                              clean_repeating_characters, clean_kaomoji, clean_brackets,
                              clean_commas, clean_numbers,
                              clean_double_hyphens, clean_ellipses, clean_full_stops,
                              clean_wave_dash, clean_sentence_end,
                              clean_misc_characters, tokenize_text)


def clean(text: str) -> str:
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


def clean_and_tokenize(text: str) -> str:
    """Cleans text using the functions found in the helpers sub-directory,
    and tokenizes to sentences

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
    tokens, text = tokenize_text(text, remove_stop_words=True, lemmatize=True)
    return tokens


test_text = open("test.txt", "r", encoding="utf-8").read()
# save
with open("cleaned.txt", "w", encoding="utf-8") as f:
    f.write(clean(test_text))
with open("tokenized.txt", "w", encoding="utf-8") as f:
    f.write(clean_and_tokenize(test_text))
