#!/usr/bin/bash

export BASE_CONFIG_FILE=./test
export EMU_CONFIG_FILE=./test
export USER_CONFIG_FILE=./test
export CONFIG_SAVE_DIR=./
export SVG_FILE=./test/demo.svg
export DEFAULT_MODE=default

echo $SVG_FILE

cd /home/czh/github/cbs_smt/verif_config; python2 -m CGIHTTPServer 8008
