import re

import neologdn
from mojimoji import han_to_zen

ESCAPE_CODES = [r'&lt;', r'&gt;', r'&amp;', r'&quot;', r'&nbsp;', r'&copy;']

HIRAGANA = r'\u3041-\u3096'
KATAKANA = r'\u30A1-\u30F6'
PROLONGED_SOUND_MARK = r'\u30FC'
KANJI = r'\u3005\u4E00-\u9FFF'

WHITELIST_PTN = re.compile(rf'[a-zA-Z0-9!?()「」、。{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]')
JP_PTN = re.compile(rf'[{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]')


def clean_text(text: str, twitter: bool) -> str:
    cleaned_text = _normalize(text=text)
    if _is_japanese(cleaned_text):
        if twitter:
            cleaned_text = _twitter_preprocess(text=cleaned_text)
        cleaned_text = _filter(text=cleaned_text)
    return han_to_zen(cleaned_text)


def _normalize(text: str, repeat: int = 2) -> str:
    return neologdn.normalize(text, repeat=repeat)


def _is_japanese(string):
    al_num = re.compile(r'^[a-zA-Z0-9()!?,.:;\-\'\"\s]+$')
    result = not(al_num.match(string) is not None)
    return result


def _twitter_preprocess(text: str) -> str:
    replaced_text = re.sub(r'[RT]\w+', '', text)
    replaced_text = re.sub(r'[@][a-zA-Z0-9_]+', '', replaced_text)
    replaced_text = re.sub(r'#(\w+)', '', replaced_text)
    return replaced_text


def _replace_punctuation(text: str) -> str:
    replaced_text = re.sub(r'([、。])、+', r'\1', text)
    replaced_text = re.sub(r'([、。])。+', '。', replaced_text)
    replaced_text = re.sub(r'^[、。!?]', '', replaced_text)
    replaced_text = re.sub(
        rf'。[a-zA-Z0-9!?「」{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]。', '。', replaced_text)
    return replaced_text


def _whitelist_filter(text: str) -> str:
    """
    あいうw → あいう。
    (あいう)w → (あいう)。
    あいう → あいう。
    あいう☆ → あいう。
    あいう。w 。→ あいう。。。

    """
    ptn = re.compile(rf'[0-9。w{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]')
    filtered_text = ''
    for i, character in enumerate(text):
        if WHITELIST_PTN.match(character) and \
                not (character == 'w' and text and ptn.match(filtered_text[-1])):
            filtered_text += character
            continue
        filtered_text += '。'
    filtered_text += '。'
    return filtered_text


def _delete_kaomoji(text: str) -> str:
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
    text = re.sub(r'(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?', '', text)
    for escape_code in ESCAPE_CODES:
        text = re.sub(escape_code, '', text)
    text = _whitelist_filter(text=text)
    text = _replace_punctuation(text)

    text = re.sub(r'笑笑+', '笑', text)
    text = re.sub(r'笑。', '。', text)

    text = re.sub(r'([!?。])[a-zA-Z0-9]+([!?。])', r'\1\2', text)
    text = _replace_punctuation(text)

    text = _delete_kaomoji(text)
    text = _replace_punctuation(text)

    text = re.sub(r'(。\))|(\(。)', '。', text)
    text = re.sub(r'[。!?][ノシﾉｼ]+[。!?]', '。', text)
    text = re.sub(r'。([!?])', r'\1', text)
    text = re.sub(r'([!?])。', r'\1', text)
    text = _replace_punctuation(text)

    text = re.sub(r'!!+', '!', text)
    text = re.sub(r'\?\?+', '?', text)
    text = re.sub(r'^.。', '', text)
    text = '' if len(text) == 1 else text

    return text
