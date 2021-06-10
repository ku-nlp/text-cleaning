import sys
from argparse import ArgumentParser

from joblib import Parallel, delayed

from clean_text import clean_text

DELIMITER = {'txt': None, 'csv': ',', 'tsv': '\t'}
JOINER = {'txt': '', 'csv': ',', 'tsv': '\t'}


def _clean_texts(input_text, file_format, twitter):
    delimiter = DELIMITER[file_format]
    joiner = JOINER[file_format]
    return joiner.join([clean_text(text=text, twitter=twitter) for text in input_text.split(delimiter)])


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file-format', default='txt', type=str, choices=['txt', 'csv', 'tsv'])
    parser.add_argument('-n', '--n-jobs', default=1, type=int)
    parser.add_argument('-t', '--twitter', action='store_true')
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

    outputs = Parallel(n_jobs=args.n_jobs, verbose=10)(
        [delayed(_clean_texts)(input_text, args.file_format, args.twitter) for input_text in input_texts])
    for output in outputs:
        print(output)


if __name__ == '__main__':
    main()
