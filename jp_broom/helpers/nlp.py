"""
Functions related to Natural Language Processing (NLP). Mainly to
create a separate space for Spacy related functions.
"""
import spacy

nlp = spacy.load("ja_core_news_md")


def tokenize_text(text: str, remove_stop_words=True, lemmatize=True) -> str:
    """
    Tokenizes text using spaCy, with options to remove stop words and lemmatize.

    Args:
        text (str): Input text.
        remove_stop_words (bool): Whether to remove stop words. Defaults to True.
        lemmatize (bool): Whether to lemmatize the text. Defaults to True.

    Returns:
        str: Processed text, processed text as tokens
    """
    doc = nlp(text)
    tokens = []

    for token in doc:
        if remove_stop_words and token.is_stop:
            continue
        if lemmatize:
            tokens.append(token.lemma_)
        else:
            tokens.append(token.text)

    return " ".join(tokens), tokens
