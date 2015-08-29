MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
TOP_DIR := $(patsubst %/,%,$(dir $(MKFILE_PATH)))

.PHONY: all vendor binaries

all:
	@echo "make vendor"
	@echo "make run.fcserver"
	@echo "make run.dev.fcserver"


run.fcserver:
	./vendor/fadecandy/bin/fcserver-rpi config/2015-burning-man/fcserver.json

run.dev.fcserver:
	./vendor/fadecandy/bin/fcserver-rpi config/2015-burning-man/fcserver-dev.json

##################################################
# vendor

VENDOR=./scripts/vendor-git-repo.sh

vendor:
	$(VENDOR) fadecandy git@github.com:scanlime/fadecandy.git \
		f8907cad4aa4f184faa2fd4c9e1832175733e27d
	$(VENDOR) openpixelcontrol git@github.com:zestyping/openpixelcontrol.git \
		dbf4b54fe70c28b6e926697ee732d483edbd77e9
