import sys
from argparse import ArgumentParser
from typing import Optional

from jp_broom import clean_text

DELIMITER = {'txt': None, 'csv': ',', 'tsv': '\t'}
JOINER = {'txt': '', 'csv': ',', 'tsv': '\t'}


def _clean_texts(input_text: str, file_format: str, twitter: bool, han2zen: bool) -> str:
    """Cleans input text

    Args:
        input_text: Input text as string
        file_format: File format of input text
        twitter: Whether to perform twitter-specific cleaning
        han2zen: Whether to convert hankaku (half-width) characters to zenkaku
         (full-width)

    Returns:
        Cleaned text as string
    """
    delimiter: Optional[str] = DELIMITER[file_format]
    joiner: str = JOINER[file_format]
    return joiner.join(clean_text(text, twitter=twitter, han2zen=han2zen) for text in input_text.split(delimiter))


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file-format', default='txt', type=str, choices=['txt', 'csv', 'tsv'])
    parser.add_argument('-n', '--n-jobs', default=1, type=int)
    parser.add_argument('-t', '--twitter', action='store_true', help='perform twitter-specific cleaning')
    parser.add_argument('--han2zen', '--h2z', action='store_true', help='convert hankaku characters to zenkaku ones')
    parser.add_argument('-i', '--input-file', type=str)
    args = parser.parse_args()

    input_texts = []
    with open(args.input_file, 'rb') if args.input_file else sys.stdin as f:
        for line in f.buffer:
            try:
                line = line.decode('utf-8')
            except UnicodeDecodeError:
                line = ''
            input_texts.append(line.strip())

    outputs = [_clean_texts(input_text, args.file_format, args.twitter, args.han2zen) for input_text in input_texts]
    for output in outputs:
        print(output)


if __name__ == '__main__':
    main()
