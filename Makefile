INPUT_DIR := /somewhere/input
OUTPUT_DIR := /somewhere/output
# input file format. txt or csv or tsv
FILE_FORMAT := txt
NUM_JOBS_PER_MACHINE := 10
TWITTER :=
PYTHON :=

INPUT_FILES := $(shell find $(INPUT_DIR) -type f)
REL_PATHS := $(patsubst $(INPUT_DIR)/%,%,$(INPUT_FILES))
INPUT_EXT := $(suffix $(word 1, $(INPUT_FILES)))

CAT := cat
CATOUT := cat
ifeq ($(INPUT_EXT),.gz)
	CAT := zcat
	CATOUT := gzip
endif
ifeq ($(INPUT_EXT),.zip)
	CAT := zcat
	CATOUT := zip
endif
ifeq ($(INPUT_EXT),.bz2)
	CAT := bzcat
	CATOUT := bzip2
endif

ifndef PYTHON
	PYTHON := $(shell which python)
endif

CLEANED_FILES := $(addprefix $(OUTPUT_DIR)/,$(REL_PATHS))

CLEANING_ARGS = --file-format $(FILE_FORMAT)
CLEANING_ARGS += --n-jobs $(NUM_JOBS_PER_MACHINE)
ifdef TWITTER
	CLEANING_ARGS += --twitter
endif

.PHONY: all
all: $(CLEANED_FILES)

$(CLEANED_FILES): $(OUTPUT_DIR)/%: $(INPUT_DIR)/%
	mkdir -p $(dir $@)
	$(CAT) $< | $(PYTHON) src/text_cleaning/main.py $(CLEANING_ARGS) | $(CATOUT) > $@ || rm $@
