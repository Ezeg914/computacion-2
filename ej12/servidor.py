#!/usr/bin/python3
import socket
import sys
import time
import getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:')

print('opciones: ', opt)

p = ""

for (op, ar) in opt:
    if (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = p

server_socket.bind((host, port))
server_socket.listen(5)



while True:
    conn, addr = server_socket.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Address: %s - Port: %d' % (addr[0], addr[1]))
        print('Recibido: '+data.decode('ascii').upper())
        
        time.sleep(1)

    conn.close()
    print('client disconnect')