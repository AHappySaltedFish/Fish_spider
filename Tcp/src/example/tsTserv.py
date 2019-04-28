'''
Created on 2019��4��20��

@author: 24439
'''
# coding=gbk
from socket import *
from time import ctime

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        #data = tcpCliSock.sendall(data)
        if not data:
            break
        b =  ctime().encode()
        print(type(data))
        tcpCliSock.send(ctime().encode() + (' ').encode() + data)
    tcpCliSock.close()
tcpSerSock.close()