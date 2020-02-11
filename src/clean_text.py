import neologdn


def clean_text(text):
    normalized_text = _normalize(text=text)
    return normalized_text


def _normalize(text, repeat=2):
    return neologdn.normalize(text, repeat=repeat)
