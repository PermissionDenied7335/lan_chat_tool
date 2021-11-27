#!/usr/bin/env python3
from socket import *
HOST = ""
PORT = 9999
ADDR = (HOST, PORT)
BUFF = 1024
recv = socket(AF_INET, SOCK_DGRAM)
recv.bind(ADDR)
try:
    while True:
        data, addr = recv.recvfrom(BUFF)
        print(str(addr) + data.decode("utf-8"))
except Exception as e:
    recv.close()
    exit(0)
finally:
    recv.close()
    exit(0)
