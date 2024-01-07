"""
Functions related to Natural Language Processing (NLP). Mainly to
create a separate space for Spacy related functions.
"""
import spacy
from spacy import Language


def load_spacy_model(model_name: str = "ja_core_news_md") -> Language:
    """Loads a Spacy model

    Args:
        model_name: Name of the model to load (default is "ja_ginza")

    Returns:
        Spacy Language object
    """
    return spacy.load(model_name)
