#!/usr/bin/env python3
# coding: utf-8

import socket

s = socket.socket(socket.AF_ INET, socket.SOCK_ DGRAM)
#s. connect(('127.0.0.1' ,8088))

print('I am connecting the server!')

for data in ['aBch','f服务d','h7Tq','.']:

s. sendto(data.encode('utf-8'),('127.0.0.1', 8088))

str1 = s.recv(1024).decode( 'utf-8')

print('The original string is:',data,'\tthe processed string s:',str1)

s.close()
