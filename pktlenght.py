import sys
import os
import socket
import time
import select
import socket
import numpy as np

HOST = '127.0.0.1'  
PORT = 1337       

def recv_pkt(s):
    addr=b""
    while(len(addr)<6):
        addr=addr+s.recv(1)
    lenght=addr[-1]
    #print(lenght)
    while(len(addr)<lenght):
        addr=addr+s.recv(1)
    return(addr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    pkt=b"\x2a"
    for i in range(300):
        pkt=pkt+bytes([0])
        s.send(pkt)
        addr = recv_pkt(s)
        if not b"Command" in addr:
            print(i)
            print("packet : ")
            print(pkt)
            print("reponse du serveur : ")
            print(addr)
            print("reponse du serveur decodée: ")
            print(addr.decode())
        