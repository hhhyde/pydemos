'''
Created on 2012-12-26

@author: k0000010359
'''
import socket
s = socket.socket()
s.connect(('192.168.41.55', 9992))
s.sendall('id:123')
print(s.recv(1000))
