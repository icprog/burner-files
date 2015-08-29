MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
TOP_DIR := $(patsubst %/,%,$(dir $(MKFILE_PATH)))

.PHONY: all vendor

all:
	@echo "make vendor"


##################################################
# vendor

VENDOR=./scripts/vendor-git-repo.sh

vendor:
	$(VENDOR) fadecandy git@github.com:scanlime/fadecandy.git \
		f8907cad4aa4f184faa2fd4c9e1832175733e27d
	$(VENDOR) openpixelcontrol git@github.com:zestyping/openpixelcontrol.git \
		dbf4b54fe70c28b6e926697ee732d483edbd77e9
