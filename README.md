# text-cleaning

## Requirements
- Python 3.6.5
- mojimoji
- neologdn
- joblib

## How to run

    $ gxpc make -j 10 INPUT_DIR=/somewhere OUTPUT_DIR=/somewhere/out -- (gxp options)

Options:

- FILE_FORMAT=txt: Format of input file (txt or csv or tsv)
- NUM_JOBS_PER_MACHINE=10: The maximum number of concurrently running jobs per machine
- TWITTER=1: Perform twitter specific cleaning
