#!/usr/bin/python3
import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 8005

client_socket.connect((host, port))




while True:
    msg = input('> ').encode()
    try:
        client_socket.sendto(msg, (host, port))
    except socket.error:
        print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()
    print(client_socket.recv(1024).decode())

