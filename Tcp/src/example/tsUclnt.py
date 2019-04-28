'''
Created on 2019年4月22日

@author: 24439
'''
from socket import *
HOST = 'localhost'
PORT = 8081
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf8'),ADDR)
    
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print('服务器say:%s'% data.decode('utf8'))
    
udpCliSock.close()