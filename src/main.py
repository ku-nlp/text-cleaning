import sys
from argparse import ArgumentParser

from joblib import Parallel, delayed

from clean_text import clean_text


def _clean_texts(input_text, delimiter, twitter):
    if input_text:
        print(delimiter.join([clean_text(text=text, twitter=twitter) for text in input_text.split(delimiter)]))


def main():
    parser = ArgumentParser()
    parser.add_argument('-d', '--delimiter', default='\t', type=str)
    parser.add_argument('-n', '--n_jobs', default=10, type=int)
    parser.add_argument('-t', '--twitter', action='store_true')
    parser.add_argument('-i', '--input-file', type=str)
    args = parser.parse_args()

    if args.input_file is not None:
        with open(args.input_file, 'r') as f:
            input_texts = f.read()
    else:
        input_texts = ''.join(sys.stdin.readlines())

    Parallel(n_jobs=args.n_jobs, verbose=10)([delayed(_clean_texts)(input_text, args.delimiter, args.twitter)
                                              for input_text in input_texts.split('\n')])


if __name__ == '__main__':
    main()
