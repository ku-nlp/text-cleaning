import re

import neologdn
from mojimoji import han_to_zen

WHITELIST_SYMBOL = ['!', '?', '(', ')', '（', '）', '「', '」']
ESCAPE_CODES = [r'&lt;', r'&gt;', r'&amp;', r'&quot;', r'&nbsp;', r'&copy;']


def clean_text(text, twitter):
    cleaned_text = _normalize(text=text)
    if twitter:
        cleaned_text = _twitter_preprocess(text=cleaned_text)
    cleaned_text = _whitelist_filter(text=cleaned_text)
    return han_to_zen(cleaned_text)


def _normalize(text, repeat=2):
    return neologdn.normalize(text, repeat=repeat)


def _twitter_preprocess(text):
    replaced_text = re.sub(r'[RT]\w+', '', text)
    replaced_text = re.sub(r'[@][a-zA-Z0-9_]+', '', replaced_text)
    replaced_text = re.sub(r'#(\w+)', '', replaced_text)
    return replaced_text


def _whitelist_filter(text):
    removed_text = re.sub(r'(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?', '', text)
    for escape_code in ESCAPE_CODES:
        removed_text = re.sub(escape_code, '', removed_text)

    whitelist_ptn = re.compile(r'[a-zA-Z0-9\u3041-\u309F\u30A1-\u30FF\u4E00-\u9FFF]')
    jp_ptn = re.compile(r'[0-9\u3041-\u309F\u30A1-\u30FF\u4E00-\u9FFF。]')

    filtered_text = ""
    for i, character in enumerate(removed_text):
        if whitelist_ptn.match(character):
            if character == 'w' and filtered_text and jp_ptn.match(filtered_text[-1]):
                filtered_text += '。'
            else:
                filtered_text += character
        elif character in WHITELIST_SYMBOL:
            filtered_text += character
        else:
            filtered_text += '。'
    filtered_text += '。'

    filtered_text = re.sub(r'。。+', '。', filtered_text)
    filtered_text = re.sub(r'^。', '', filtered_text)

    filtered_text = re.sub(r'笑笑+', r'笑', filtered_text)
    filtered_text = re.sub(r'笑。', '。', filtered_text)

    filtered_text = re.sub(r'([!\?。])[a-zA-Z0-9]+([!\?。])', r'\1\2', filtered_text)
    filtered_text = re.sub(r'。。+', '。', filtered_text)
    filtered_text = re.sub(r'^。', '', filtered_text)
    filtered_text = re.sub(r'\(。\)', '', filtered_text)
    filtered_text = re.sub(r'\（。\）', '', filtered_text)
    filtered_text = re.sub(r'\「。\」', '', filtered_text)
    filtered_text = re.sub(r'。。+', '。', filtered_text)
    filtered_text = re.sub(r'^。', '', filtered_text)

    filtered_text = re.sub(r'。([!\?])', r'\1', filtered_text)
    filtered_text = re.sub(r'([!\?])。', r'\1', filtered_text)

    filtered_text = re.sub(r'!!+', '!', filtered_text)
    filtered_text = re.sub(r'\?\?+', '?', filtered_text)

    return filtered_text
