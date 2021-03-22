import sys
import os
import socket
import time
import select
import socket
import numpy as np
import string
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
    liste=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    #listetemps=np.zeros((30,16))
    #listetempsfinal=[]
    #cara3=liste[i]
    """c1=b"0"
    c2=b"3"
    c3=b"3"
    c4=b"8"
    c5=b"d"
    c6=b"3"
    c7=b"4"
    c8=b"8"
    pkt=bytes([37])
    pkt=pkt+c1+c2+c3+c4+c5+c6+c7+c8
    s.send(pkt)
    addr = recv_pkt(s)
    print(addr)"""
    #payload=b"\xac\x00\x00\x00\x0c\x00\x00\x00\x39\x00\x00\x00\x54\x65\x70\x6f\x63\x68\x3d\x31\x30\x30\x32\x30\x31\x31\x0a\x75\x75\x69\x64\x3d\x32\x36\x36\x37\x2d\x32\x38\x35\x61\x2d\x34\x64\x39\x65\x0a\x67\x72\x6f\x75\x70\x3d\x75\x73\x65\x72\x0a\x44\x33\x37\x41\x45\x35\x30\x46\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41"
    #payload=b"*logdl 101732"
    #i=bytes([i])
    payload=b"\x40\x14\x53\x7a\x40\x02"
    s.send(payload)
    addr = recv_pkt(s)
    print("packet : ")
    print(payload)
    print("reponse du serveur : ")
    print(addr)
    print("\n\n")
    time.sleep(5)
    print("reponse du serveur decodée: ")
    print(addr.decode())