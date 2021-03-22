import sys
import os
import socket
import time
import select
import socket

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
    for i in range(256):                                   
        pkt=bytes([i])
        s.send(pkt)
        addr = recv_pkt(s)
        if not b"Unknown" in addr:
            print("reponse du serveur : ")
            print(addr)

                    

    