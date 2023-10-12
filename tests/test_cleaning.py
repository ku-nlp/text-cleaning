import os
import glob
import json
from typing import Tuple

import pytest

from src.text_cleaning import clean_text


def read_test_file(path: str) -> Tuple[str, str]:
    with open(path, encoding='utf-8') as f:
        dct = json.load(f)
        return dct['input_text'], dct['output_text']


test_file_path_pattern = os.path.join(os.path.dirname(__file__), 'test_cleaning', '*.json')
test_cases = [read_test_file(path) for path in sorted(glob.glob(test_file_path_pattern))]


@pytest.mark.parametrize('test_case', test_cases)
def test_clean_text(test_case):
    input_text, output_text = test_case
    assert clean_text(input_text, twitter=True, han2zen=True) == output_text
