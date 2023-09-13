#!/usr/bin/env python2
# _*_ coding: UTF-8 _*_

import os
import sys
import json
import cgi, cgitb
import tool
from log import log

n = int(os.environ["CONTENT_LENGTH"])
req = sys.stdin.read(n)
# form = cgi.FieldStorage() #can not use with post data
# action = form.getvalue("action")
action = os.environ["QUERY_STRING"]

print "Content-type: text/plain\r\n"

log("server action[%s]" % action)

if action == "LoadHtml" :
    print tool.LoadHtml(req)
    sys.exit()

req = json.loads(req)
# action = req["action"]

if action == "LoadSvg" :
    print tool.LoadSvg(req["fileContent"], req["skt"])
    sys.exit()

# 第一次获取<ul>
if action == "GetHtml":
    print tool.GetHtml('default')
    sys.exit()

# 第一次获取svg
if action == "GetSvg":
    print tool.GetSvg('default', req["skt"])
    sys.exit()

if action == "getlog":
    print tool.GetLog(req["configs"], req["config"])

if action == "save":
    print tool.Save(req["fileName"], req["configs"], req["overwrite"])
