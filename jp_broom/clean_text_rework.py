"""
DONE:
- Text width conversion
- Punctuation standardisation/removal

TODO:

- Kaomoji removal (find a kaomoji dictionary somewhere)
- Remove non-Japanese characters (e.g. ✋)
- Remove english
- Remove katakana
- Remove URLs / HTML tags / email addresses
- Remove quotation symbols (e.g. 「」)
- Remove repeating characters (e.g. !!!!!)
- Removing special characters (find out which symbols the japanese use)
- Remove/Trim whitespace
- Remove stop words
- Lemmatization
- Remove laughter expressions (e.g. 笑笑笑 and wwwww)
- Tokenization
- Kanji to kana?
- Remove numbers?
- Casing? Not sure if this is relevant, but maybe if you want to keep english in the text

References:
    https://en.wikipedia.org/wiki/Japanese_punctuation
    https://en.wikipedia.org/wiki/Japanese_typographic_symbols

"""

from mojimoji import han_to_zen


def normalize_width(text: str) -> str:
    """Converts hankaku (half-width) characters to zenkaku (full-width)

    Args:
        text: Input text

    Returns:
        Text with hankaku characters converted to zenkaku
    """
    return han_to_zen(text)


def convert_punctuation(text: str) -> str:
    """Converts punctuation to a single choice of punctuation

    Args:
        text: Input text

    Returns:
        Text with punctuation converted to a single choice of punctuation
    """




def normalize_punctuation(text: str) -> str:
    """Normalize punctation, by converting to a single choice of punctuation, and
    removing repeating punctuation.

    Args:
        text:

    Returns:

    """
    ...


