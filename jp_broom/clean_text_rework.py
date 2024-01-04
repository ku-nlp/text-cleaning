"""
This file will contain functions that clean text using the functions found in the helpers sub-directory.
"""
from jp_broom.helpers import (normalize_width, clean_whitespace, clean_laughter,
                              clean_repeating_characters, clean_kaomoji, clean_brackets,
                              clean_commas, clean_numbers,
                              clean_double_hyphens, clean_ellipses, clean_full_stops,
                              clean_wave_dash)


# TODO: split this into two functions
def clean_text(text: str,
               normal_clean: bool = True) -> str:
    """Cleans text using the functions found in the helpers sub-directory.

    Args:
        text: Input text
        normal_clean: If True, just make text more readable, if false, switch to
        tokenizing mode.

    Returns:
        Cleaned text
    """
    if normal_clean:
        text = normalize_width(text)
        text = clean_kaomoji(text)
        text = clean_laughter(text, remove=False)
        text = clean_repeating_characters(text, min_repeats=3, remove=False)
        text = clean_brackets(text, remove=False)
        text = clean_commas(text, remove=False, convert=False)
        text = clean_double_hyphens(text, remove=False)
        text = clean_ellipses(text, remove=False)
        text = clean_full_stops(text, remove=False, convert=False)
        text = clean_wave_dash(text, remove=False)
        text = clean_numbers(text, remove=False, convert=True)
        text = clean_whitespace(text, remove=False, convert=False)
        return text
    else:
        text = normalize_width(text)
        text = clean_kaomoji(text)
        text = clean_laughter(text, remove=True)
        text = clean_repeating_characters(text, min_repeats=3, remove=True)
        text = clean_brackets(text, remove=True)
        text = clean_commas(text, remove=False, convert=True)
        text = clean_double_hyphens(text, remove=True)
        text = clean_ellipses(text, remove=True)
        text = clean_full_stops(text, remove=False, convert=True)
        text = clean_wave_dash(text, remove=True)
        text = clean_numbers(text, remove=True, convert=False)
        text = clean_whitespace(text, remove=False, convert=True)
        return text


test_text = open("test.txt", "r", encoding="utf-8").read()
# save
with open("cleaned.txt", "w", encoding="utf-8") as f:
    f.write(clean_text(test_text, normal_clean=True))
with open("tokenized.txt", "w", encoding="utf-8") as f:
    f.write(clean_text(test_text, normal_clean=False))
