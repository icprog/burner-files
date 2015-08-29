MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
TOP_DIR := $(patsubst %/,%,$(dir $(MKFILE_PATH)))

.PHONY: all vendor binaries build config

all:
	@echo "make vendor"
	@echo "make build"
	@echo "make config"
	@echo "make run.fcserver"
	@echo "make run.dev.fcserver"
	@echo "make run.glserver"

build: bin.fcserver

config:
	cd 2015-burning-man && python gen-layout.py

bin.fcserver:
	mkdir -p bin

# Replicate fadecandy .gitmodules
	cd vendor/fadecandy/server && rm -rf libusbx && ln -fs ../../libusbx
	cd vendor/fadecandy/server && rm -rf libwebsockets && ln -fs ../../libwebsockets
	cd vendor/fadecandy/server && rm -rf rapidjson && ln -fs ../../rapidjson

# Set TERM='' for the build because otherwise one of Python modules outputs junk
# junk escape sequence on some platforms when imported.  This breaks FC's manifest.py.
	cd vendor/fadecandy/server && make TERM='' && mv fcserver $(TOP_DIR)/bin/

run.fcserver:
	./bin/fcserver 2015-burning-man/fcserver.json

run.dev.fcserver:
	./bin/fcserver 2015-burning-man/fcserver-dev.json

run.glserver:
	./vendor/openpixelcontrol/bin/gl_server -l 2015-burning-man/glserver-layout.json

##################################################
# vendor

VENDOR=./scripts/vendor-git-repo.sh

vendor:
	$(VENDOR) fadecandy git@github.com:scanlime/fadecandy.git \
		f8907cad4aa4f184faa2fd4c9e1832175733e27d
	$(VENDOR) openpixelcontrol git@github.com:zestyping/openpixelcontrol.git \
		dbf4b54fe70c28b6e926697ee732d483edbd77e9
	$(VENDOR) libusbx https://github.com/scanlime/libusbx.git \
		6899a2647f9cff79d839587a0b81780bdbb13b40
	$(VENDOR) libwebsockets https://github.com/scanlime/libwebsockets.git \
		8028bdf25c2780ec4d931b195fea70e4e8269125
	$(VENDOR) rapidjson git@github.com:scanlime/rapidjson.git \
	       	0c69df5ac098640018d9232ae71ed1036c692187
