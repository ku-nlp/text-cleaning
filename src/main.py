import sys
from argparse import ArgumentParser

from joblib import Parallel, delayed

from clean_text import clean_text


def _clean_texts(input_text, splitter, twitter):
    if input_text:
        if splitter == 's':
            print(clean_text(text=input_text, twitter=twitter))
        elif splitter == 'sts':
            former, latter = input_text.split('\t')
            cleaned_former = clean_text(text=former, twitter=twitter)
            cleaned_latter = clean_text(text=latter, twitter=twitter)
            print(f'{cleaned_former}\t{cleaned_latter}')


def main():
    parser = ArgumentParser()
    parser.add_argument('-s', '--splitter', default='s', type=str, choices=['s', 'sts'])
    parser.add_argument('-n', '--n_jobs', default=10, type=int)
    parser.add_argument('-t', '--twitter', action='store_true')
    parser.add_argument('-i', '--input-file', type=str)
    args = parser.parse_args()

    if args.input_file is not None:
        with open(args.input_file, 'r') as f:
            input_texts = f.read()
    else:
        input_texts = ''.join(sys.stdin.readlines())

    Parallel(n_jobs=args.n_jobs, verbose=10)([delayed(_clean_texts)(input_text, args.splitter, args.twitter)
                                              for input_text in input_texts.split('\n')])


if __name__ == '__main__':
    main()
