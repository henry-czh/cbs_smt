export MAIN_CFG_FILE=/home/czh/github/cbs_smt/verif_config/test/all.cfg
export USR_CFG_FILE=/home/czh/github/cbs_smt/verif_config/test/usr.cfg
export CFG_SAVE_DIR=/home/czh/github/cbs_smt
#export SVG_FILE=/home/czh/github/cbs_smt/verif_config/test/demo.svg
export SVG_FILE=/home/czh/github/cbs_smt/arch.svg
export HTML_FILE=/home/czh/github/cbs_smt/verif_config/config.html
export CBS_HOME=.
export DEFAULT_MODE=default
python3 main.py --disable-seccomp-filter-sandbox
