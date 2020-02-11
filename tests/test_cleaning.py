import glob
import json
import typing
import pytest

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import clean_text


def read_test_file(path):
    """Read a test file.

    Parameters
    ----------
    path : str
        The path to a test file.

    Returns
    -------
    typing.Tuple[str, str]
    """
    with open(path) as f:
        dct = json.load(f)
        return dct['input_text'], dct['output_text']


test_file_path_pattern = os.path.join(os.path.dirname(__file__), 'test_cleaning', '*.json')
test_cases = [read_test_file(path) for path in sorted(glob.glob(test_file_path_pattern))]


@pytest.mark.parametrize('test_case', test_cases)
def test_clean_text(test_case):
    input_text, output_text = test_case
    assert clean_text(input_text) == output_text
