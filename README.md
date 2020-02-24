# text-cleaning: A Japanese powerful text cleaner

## Description
This project cleans dirty Japanese texts, which include a lot of emoji and kaomoji
in a whitelist method.

## Cleaning Example

### Before:

```text
dirty text
```

### After:

```text
cleaned text
```

## Requirements
- Python 3.6.5
- mojimoji
- neologdn
- joblib

## How to Run

### Using python script directly

```zsh
cat input.txt | python src/main.py <options> > output.txt
```

### Using makefile
When input files are located in directories hierarchically you can clean
them keeping directory structure by using makefile.  
If input is compressed files, Makefile detect their format from their
suffix and output cleaned files in the same format.

```zsh
make INPUT_DIR=/somewhere OUTPUT_DIR=/somewhere/out PYTHON=/somewhere/.venv/bin/python
```

Options:

- FILE_FORMAT=txt: Format of input file (txt or csv or tsv)
- NUM_JOBS_PER_MACHINE=10: The maximum number of concurrently running jobs per machine
- TWITTER=1: Perform twitter specific cleaning
- PYTHON: Path to python interpreter of virtual environment
