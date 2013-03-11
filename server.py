#!/usr/bin/env python
import os
import signal
import socket

signal.signal(signal.SIGPIPE, signal.SIG_IGN)

sock = socket.socket(socket.AF_UNIX)
os.unlink('test.uds')
sock.bind('test.uds')
sock.listen(10)

while True:
    s, addr = sock.accept()
    print "connected from:", addr
    while True:
        s.sendall("a"*60 + '\n')
