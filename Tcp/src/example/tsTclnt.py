'''
Created on 2019��4��20��

@author: 24439
'''
# coding=gbk
from socket import *

HOST = 'localhost'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    
    print(data.decode('utf8'))
tcpCliSock.close()