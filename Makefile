INPUT := /somewhere/tsv/sentences/directory
OUTPUT := /somewhere/out
SPLITTER := ""
JUMANPP :=

SHELL = /bin/bash -eu
#PYTHON := $(shell which python)
JUMAN_COMMAND := /mnt/orange/ubrew/data/bin/jumanpp

INPUT_FILES := $(wildcard $(INPUT)/**/*.*)
REL_PATHS := $(patsubst INPUT/%,%,$(INPUT_FILES))
TEXT_DIR := $(OUTPUT)/text
JUMAN_DIR := $(OUTPUT)/jumanpp

INPUT_EXT := $(suffix $(word 1, $(INPUT_FILES)))
CAT := cat
ifeq ($(INPUT_EXT),gz)
	CAT := zcat
endif

CLEANED_FILES := $(addprefix $(TEXT_DIR),$(REL_PATHS))
JUMANPP_FILES := $(addprefix $(JUMAN_DIR),$(REL_PATHS))

.PHONY: all
ifdef JUMANPP
all: $(JUMANPP_FILES)
else
all: $(CLEANED_FILES)
endif

$(JUMANPP_FILES): /$(TEXT_DIR)/%: $(JUMAN_DIR)/%
	mkdir -p $(dir $@)
	cat $< | ./scripts/jumanpp.sh > $@ || rm $@

$(CLEANED_FILES): /$(INPUT)/%: $(TEXT_DIR)/%
	mkdir -p $(dir $@)
	$(CAT) $< | ./scripts/clean.sh > $@ || rm $@
