#!/usr/bin/python3
import socket, sys, time, getopt, os

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:')

print('opciones: ', opt)


p = ""
t = ""
f = ""
j = ""


for (op, ar) in opt:
    if (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    elif (op == '-t'):
        t = str(ar)
        if t == 'tcp':
            j = socket.SOCK_STREAM
            print('Opcion -t tcp exitosa!')
        elif t == 'udp':
            j = socket.SOCK_DGRAM
            print('Opcion -t udp exitosa!')
        else:
            print('Opcion incorrecta')
    elif (op == '-f'):
        f = str('tmp/' + ar)
        print('Opcion -f exitosa!')
    else:
        print('Opcion incorrecta!')

server_socket = socket.socket(socket.AF_INET, j)

host = ""
port = p

server_socket.bind((host, port))
server_socket.listen(5)



while True:
    conn, addr = server_socket.accept()
    while True:
        data = conn.recv(1024).decode('ascii')
        if not data: break
        with open(f,'w') as file:
            file.write(str(data))
    conn.close()
    print('client disconnect')