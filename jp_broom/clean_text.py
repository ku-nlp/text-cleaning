import re

import neologdn
from mojimoji import han_to_zen

ESCAPE_CODES = [r'&lt;', r'&gt;', r'&amp;', r'&quot;', r'&nbsp;', r'&copy;']

HIRAGANA = r'\u3041-\u3096'
KATAKANA = r'\u30A1-\u30F6'
PROLONGED_SOUND_MARK = r'\u30FC'
KANJI = r'\u3006\u4E00-\u9FFF'  # U+3006: 〆
REPEATING_MARK = r'\u3005'

WHITELIST_PTN = re.compile(rf'[a-zA-Z0-9!?()「」、。{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}{REPEATING_MARK}]')
JP_PTN = re.compile(rf'[{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]')


def clean_text(text: str, han2zen: bool = True, twitter: bool = False, repeat: int = 3) -> str:
    """Clean japanese text

    Args:
        text: Input text
        han2zen: Whether to convert hankaku (half-width) characters to zenkaku
         (full-width)
        twitter: Whether to perform twitter-specific cleaning
        repeat: Number of iterations to repeat normalization

    Returns:
        Cleaned text
    """
    text = _normalize(text=text, repeat=repeat)
    if _is_japanese(text):
        if twitter is True:
            text = _twitter_preprocess(text=text)
        text = _filter(text=text)
    if han2zen is True:
        text = han_to_zen(text)
    return text


def _normalize(text: str, repeat: int) -> str:
    """Normalize text using neologdn

    Args:
        text: Input text
        repeat: Number of iterations to repeat normalization

    Returns:

    """
    return neologdn.normalize(text, repeat=repeat)


def _is_japanese(text: str) -> bool:
    """Validate if string contains japanese characters

    Args:
        text: Input text

    Returns:
        True if string contains japanese characters, False otherwise
    """
    al_num = re.compile(r'^[a-zA-Z0-9()!?,.:;\-\'\"\s]+$')
    return al_num.match(text) is None


def _twitter_preprocess(text: str) -> str:
    """Performs twitter-specific preprocessing

    Converts text to lowercase, removes RT, @mentions, #hashtags, and URLs

    Args:
        text: Input text

    Returns:
        Preprocessed text
    """
    replaced_text = re.sub(r'[RT]\w+', '', text)
    replaced_text = re.sub(r'[@][a-zA-Z0-9_]+', '', replaced_text)
    replaced_text = re.sub(r'#(\w+)', '', replaced_text)
    return replaced_text


def _replace_punctuation(text: str) -> str:
    """Replace punctuation marks

    Args:
        text: Input text

    Returns:
        Text with replaced punctuation marks
    """
    replaced_text = re.sub(r'、+', '、', text)  # "、、、" -> "、"
    replaced_text = re.sub(r'[、。]*。[、。]*', '。', replaced_text)
    replaced_text = re.sub(r'^[、。!?]', '', replaced_text)
    replaced_text = re.sub(
        rf'。[a-zA-Z0-9!?「」{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]。', '。', replaced_text)
    return replaced_text


def _whitelist_filter(text: str) -> str:
    """Converts non-whitelisted characters to '。'

    あいうw → あいう。
    (あいう)w → (あいう)。
    あいう → あいう。
    あいう☆ → あいう。
    あいう。w 。→ あいう。。。

    Args:
        text: Input text

    Returns:
        Filtered text
    """
    ptn = re.compile(rf'[0-9。w{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]')
    filtered_text = ''
    for i, character in enumerate(text):
        if WHITELIST_PTN.match(character) and \
                not (character == 'w' and filtered_text and ptn.match(filtered_text[-1])):
            filtered_text += character
            continue
        filtered_text += '。'
    filtered_text += '。'
    return filtered_text


def _delete_kaomoji(text: str) -> str:
    """Delete kaomoji (japanese emoticons) from text

    Args:
        text: Input text

    Returns:
        Text with kaomoji removed
    """
    text_ = ''
    buff = ''
    bracket_counter = 0
    for c in text:
        buff += c
        if c == '(':
            bracket_counter += 1
        elif c == ')':
            bracket_counter -= 1
            if bracket_counter == 0:
                stripped_buff = buff.lstrip('(').rstrip(')')
                if all(JP_PTN.match(c) for c in stripped_buff) and stripped_buff:
                    text_ += buff
                buff = ''
                continue
        if bracket_counter == 0:
            text_ += buff
            buff = ''
    return text_


def _filter(text: str) -> str:
    """Filter text to remove unwanted characters

    Args:
        text: Input text

    Returns:
        Filtered text
    """
    # Remove URLs
    text = re.sub(r'(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?', '', text)

    # Remove escape codes
    for escape_code in ESCAPE_CODES:
        text = re.sub(escape_code, '', text)

    # Remove non-whitelisted characters
    text = _whitelist_filter(text=text)
    text = _replace_punctuation(text)

    # remove 笑 characters if they are used as an expression of laughter (i.e. LOL)
    text = re.sub(r'笑笑+', '笑', text)
    text = re.sub(r'笑。', '。', text)

    # Remove repeating characters
    text = re.sub(r'([!?。])[a-zA-Z0-9]+([!?。])', r'\1\2', text)
    text = _replace_punctuation(text)

    # Remove kaomoji, e.g. (͡° ͜ ͡°)
    text = _delete_kaomoji(text)

    # Remove repeating punctuation marks
    text = _replace_punctuation(text)

    # Replace certain punctuation patterns (e.g. "。)" -> "。")
    text = re.sub(r'(。\))|(\(。)', '。', text)

    # Remove repeating sequences of punctuation characters
    text = re.sub(r'[。!?][ノシﾉｼ]+[。!?]', '。', text)

    # Replace certain punctuation patterns
    text = re.sub(r'。([!?])', r'\1', text)
    text = re.sub(r'([!?])。', r'\1', text)
    text = _replace_punctuation(text)

    # Replace multiple exclamation marks with a single exclamation mark
    text = re.sub(r'!!+', '!', text)

    # Replace multiple question marks with a single question mark
    text = re.sub(r'\?\?+', '?', text)

    # Remove a period at the beginning of the text
    text = re.sub(r'^.。', '', text)

    # Replace alternative numbers (０１２３４５６７８９) with regular numbers (0123456789)
    text = text.translate(str.maketrans('０１２３４５６７８９', '0123456789'))

    # Remove brackets「」
    text = re.sub(r'[「」]', '', text)

    # Check if text is empty
    text = '' if len(text) == 1 else text

    # Return text
    return text
