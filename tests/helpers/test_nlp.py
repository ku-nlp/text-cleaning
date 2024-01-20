from jp_broom.helpers import tokenize_text


def test_tokenize_text():
    """Test tokenize_text function"""
    text = "私は走っています"  # "I am running"

    # Test for stop words removal
    processed_text, tokens = tokenize_text(text, remove_stop_words=True,
                                           lemmatize=False)
    assert "は" not in tokens

    # Test for keeping stop words
    processed_text, tokens = tokenize_text(text, remove_stop_words=False,
                                           lemmatize=False)
    assert "は" in tokens

    # Test for lemmatization
    processed_text, tokens = tokenize_text(text, remove_stop_words=False,
                                           lemmatize=True)
    assert "走る" in tokens  # Assuming "走っています" gets lemmatized to "走る" ("run")

    # Test with an empty string
    text = ""
    processed_text, tokens = tokenize_text(text)
    assert processed_text == ""
    assert tokens == []


