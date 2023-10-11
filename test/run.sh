export BASE_CONFIG_FILE=/home/czh/github/cbs_smt/verif_config/test
export USER_CONFIG_FILE=/home/czh/github/cbs_smt/verif_config/test
export CONFIG_SAVE_DIR=/home/czh/github/cbs_smt
export SVG_FILE=/home/czh/github/cbs_smt/verif_config/test/demo.svg
export HTML_FILE=/home/czh/github/cbs_smt/verif_config/qtconfig.html
export DIAG_FILE=/home/czh/github/cbs_smt/test/src/test.diag
export CBS_HOME=.
export TB_HOME=/home/czh/github/cbs_smt
export DEFAULT_MODE=default

#python2 ./verif_config/cgi-bin/parseConfig.py $BASE_CONFIG_FILE $USER_CONFIG_FILE
export XDG_SESSION_TYPE=x11 #/usr/local/bin/your_soft_bin

python3 -B ../main.py --disable-seccomp-filter-sandbox
