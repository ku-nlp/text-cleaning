# jp-broom: A sopshisticated Japanese text cleaner

## Description
This project provides a simple to use text cleaner that removes most of the 
unecessary characters and symbols in Japanese text, while keeping the original 
spirit of the text intact. 

Japanese texts require different techniques from conventional western 
ones, as they tend to include:
- A mix of half-width and full-width characters
- Symbols not in the western lexicon (e.g. □)
- Kaomoji (i.e. japanese emojis  (o(*ﾟ▽ﾟ*)o) )

Original work is from https://github.com/ku-nlp/text-cleaning, but the code has been heavily modified at this point. Primary changes include:
- Conversion from a script-based to a package-based structure
- The package direction moving towards suitability for NLP projects (i.e. support Spacy)
- More features, and made more modular. If you don't like the main cleaning functions you can just used the 
underlying helper functions.
- Support for more modern versions of Python.


## Usage

```python

from jp_broom.clean_text import clean_light, clean_deep, clean_deep_tokenize

mytest_text = """
ダンジョンの秘匿は罪に当たらないが200、国民の義務に違反しているということでその後も警察の監視がつくらしい……。
"""

text_clean_light = clean_light(mytest_text)
# output = "ダョ秘匿は罪に当たらなが200、国民義務に違反てるとうことでそ後警察監視がつくら……。"
text_clean_deep = clean_deep(mytest_text)
# output = "ダョ秘匿は罪に当たらなが 国民義務に違反てるとうことでそ後警察監視がつくら"
text_clean_deep_with_nlp, tokens = clean_deep_tokenize(mytest_text)
# output = "ダョ 秘匿 罪 当たる 国民 義務 違反 てる う そ 後 警察 監視 つくる"
```

## Requirements
- Python 3.11+
- See pyproject.toml for used packages
