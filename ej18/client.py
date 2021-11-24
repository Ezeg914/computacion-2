#!/usr/bin/python3
import socket, getopt, sys


(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:c:r:')

print('opciones: ', opt)

h = ""
p = ""
c = ""
r = ""

for (op, ar) in opt:
    if (op == '-h'):
        h = str(ar)
        print('Opcion -h exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    elif (op == '-c'):
        c = str(ar)
        print('Opcion -c exitosa!')
    elif (op == '-r'):
        r = str(ar)
        print('Opcion -r exitosa!')
    else:
        print('Opcion incorrecta')


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = h
port = p

client_socket.connect((host, port))

client_socket.sendto(c.encode('ascii'), (host, port))
client_socket.sendto(r.encode('ascii'), (host, port))

