'''
Created on 2019年4月22日

@author: 24439
'''
from socket import *
from time import ctime

HOST = ''
PORT = 8081
BUFSIZ = 1024
ADDR = (HOST, PORT)

#创建套接字
udpSerSock = socket(AF_INET,SOCK_DGRAM)
#套接字与地址绑定
udpSerSock.bind(ADDR)
print('udp服务器创建成功')
try:
    while True:
        info, addr = udpSerSock.recvfrom(BUFSIZ)
        if not info:
            break
        else:
            print('客户端say:%s'% info.decode('utf8'))
            data = input('<')
            udpSerSock.sendto(data.encode('utf8'), addr)
except EOFError:
    udpSerSock.close()