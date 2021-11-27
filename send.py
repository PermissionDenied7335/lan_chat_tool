#!/usr/bin/env python3
from socket import *
PORT = 9999
send = socket(AF_INET, SOCK_DGRAM)
send.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
try:
    while True:
        data = input(">").encode("utf-8")
        send.sendto(data, ("<broadcast>", PORT))
except Exception as e:
    send.close()
    exit(0)
finally:
    send.close()
    exit(0)
