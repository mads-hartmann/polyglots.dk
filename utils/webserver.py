#!/usr/bin/env python

"""
Naive webserver that makes it easier to test front-end studpid web
pages locally before merging changes.

You have to run this from the frontend-stupid root directory.
"""

import os
from SocketServer import TCPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


def start_server():
    """Stat the http server."""

    directory = os.getcwd()
    port = 9000

    os.chdir(directory)

    tcp_server = TCPServer(
        ("", port),
        SimpleHTTPRequestHandler)

    print 'Serving from directory {} on http://localhost:{}'.format(
        os.getcwd(), port)

    tcp_server.serve_forever()

start_server()
