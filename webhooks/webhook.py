#!/usr/bin/env python
#-*- coding:utf-8 -*-

import BaseHTTPServer
import sys
import time
from subprocess import call


HOST_NAME = sys.argv[1]
PORT_NUMBER = int(sys.argv[2])
VALID_IPS = [ '192.30.252', '192.30.253', '192.30.254', '192.30.255' ]


def handle_hook():
    print "Git hook. Updating site."
    call(["git", "pull"])


class HookHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = "HookHandler/0.1"

    def do_GET(self):
        self.wfile.write('Hello!\n')
        self.send_response(200)

    def do_POST(self):
        # Check that the IP is within the GH ranges
        ip = self.client_address[0]
        valid_ip = any(ip.startswith(accepted) for accepted in VALID_IPS)
        if not valid_ip:
            self.send_error(403)

        handle_hook()

        self.send_response(200)


if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(
        (HOST_NAME, PORT_NUMBER), HookHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
