#! /bin/python

import os
import sys
import CGIHTTPServer
import SocketServer

os.environ['BASE_CONFIG_FILE'] = './test/'
os.environ['USER_CONFIG_FILE'] = './test/'
os.environ['EMU_CONFIG_FILE'] = './test/emu.cfg'
os.environ['CONFIG_SAVE_DIR'] = './test'
os.environ['SVG_FILE'] = './test/demo.svg'
os.environ['DEFAULT_MODE'] = 'default'
usr_cfg_file = os.getenv("USER_CONFIG_FILE")

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    def address_string(self):
        host, port = self.client_address[:2]
        return str(host)
    pass

Handler.extensions_map[''] = 'text/plain'

print(sys.argv)
port = int(sys.argv[1])

SocketServer.TCPServer.allow_reuse_address = True
SocketServer.TCPServer.server_name = 'zgd_server'
SocketServer.TCPServer.server_port = port

httpd = SocketServer.TCPServer(("", port), Handler)

httpd.serve_forever()

# python -m SimpleHTTPServer 8080
