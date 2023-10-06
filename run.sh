export BASE_CONFIG_FILE=/home/czh/github/cbs_smt/verif_config/test
export USER_CONFIG_FILE=/home/czh/github/cbs_smt/verif_config/test
export CONFIG_SAVE_DIR=/home/czh/github/cbs_smt
export SVG_FILE=/home/czh/github/cbs_smt/verif_config/test/demo.svg
#export SVG_FILE=/home/czh/github/cbs_smt/arch.svg
export HTML_FILE=/home/czh/github/cbs_smt/verif_config/qtconfig.html
export CBS_HOME=.
export DEFAULT_MODE=default

python2 ./verif_config/cgi-bin/parseConfig.py $BASE_CONFIG_FILE $USER_CONFIG_FILE

python3 -B main.py --disable-seccomp-filter-sandbox
