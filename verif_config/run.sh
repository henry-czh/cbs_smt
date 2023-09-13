#!/usr/bin/bash

export BASE_CONFIG_FILE=$1
export EMU_CONFIG_FILE=$2
export USER_CONFIG_FILE=$3
export CONFIG_SAVE_DIR=$4
export SVG_FILE=$5
export DEFAULT_MODE=$6

echo $SVG_FILE

#cd $7/uvs_kernel/scripts/verif_config/
python2 ./cgi-bin/parseConfig.py $BASE_CONFIG_FILE $USER_CONFIG_FILE

if [ $? -ne 0 ]; then
    exit 1
fi

port=8001
while [[ -n `netstat -tuln|grep ${port}` ]]
do
    ((port=port+1))
done

if [ $9 == "1" ]; then
    echo "mk is debug port:${port}"
    python2 -m CGIHTTPServer ${port} &
else
    echo "mk port:${port}"
    mkdir -p ~/.uvs
    python2 -m CGIHTTPServer ${port} &> ~/.uvs/cgihttp.out &
fi
pid_server=$!

# profile_path="~/.mozilla/firefox/*.user_${port}" #bash无法展开变量里的*
rm -rf ~/.mozilla/firefox/*.user_${port}/*
firefox --CreateProfile user_${port}
cp -rf ./firefox/* ~/.mozilla/firefox/*.user_${port}/
if [ -n "`firefox -v | grep -E 'Firefox (9|10)'`" ]; then
    echo '#nav-bar,#PersonalToolbar{visibility:collapse!important}' > ~/.mozilla/firefox/*.user_${port}/chrome/userChrome.css
fi
echo "user_pref('dom.input.fallbackUploadDir', '$8/config');" >> ~/.mozilla/firefox/*.user_${port}/user.js

firefox -P user_${port} http://127.0.0.1:${port}/config.html &
pid_firefox=$!
# gio open http://127.0.0.1:${port}/config.html &

function KillServer() {
    echo ' kill server and firefox'
    kill -9 $pid_server $pid_firefox
}
trap "KillServer" EXIT

wait $pid_firefox
