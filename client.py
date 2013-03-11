#!/usr/bin/env python
import socket
import time

sock = socket.socket(socket.AF_UNIX)
sock.connect('test.uds')

print sock.recv(10)
time.sleep(1000)
