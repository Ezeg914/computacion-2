#!/usr/bin/python3
import socket, getopt, sys


(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:o:n:m:')

print('opciones: ', opt)

h = ""
p = ""
o = ""
n = ""
m = ""

for (op, ar) in opt:
    if (op == '-h'):
        h = str(ar)
        print('Opcion -h exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    elif (op == '-o'):
        o = str(ar)
        print('Opcion -o udp exitosa!')
    elif (op == '-n'):
        n = str(ar)
        print('Opcion -n udp exitosa!')
    elif (op == '-m'):
        m = str(ar)
        print('Opcion -m udp exitosa!')
    else:
        print('Opcion incorrecta')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = h
port = p

client_socket.connect((host, port))

if __name__ == '__main__':
    client_socket.sendto(o.encode('ascii'), (host, port))
    client_socket.sendto(n.encode('ascii'), (host, port))
    client_socket.sendto(m.encode('ascii'), (host, port))
    data = client_socket.recv(1024).decode('ascii')
    print("Resultado", data)