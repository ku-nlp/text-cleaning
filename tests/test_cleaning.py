import glob
import json
import os
from pathlib import Path
import pytest

from src.text_cleaning import clean_text


def _read_test_file(path: str) -> tuple[str, str]:
    """Reads test file and returns input and output text.

    Args:
        path: File path to test text.

    Returns:
        Input text, expected output text
    """
    with open(path, encoding='utf-8') as f:
        dct = json.load(f)
        return dct['input_text'], dct['output_text']


test_directory = Path(__file__).parent / 'test_cleaning'
test_file_paths = test_directory.glob('*.json')
test_cases = [_read_test_file(path) for path in sorted(test_file_paths)]


@pytest.mark.parametrize('test_case', test_cases)
def test_clean_text(test_case):
    """Test clean_text function."""
    input_text, output_text = test_case
    assert clean_text(input_text, twitter=True, han2zen=True) == output_text
