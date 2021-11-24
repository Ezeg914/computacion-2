#!/usr/bin/python3
import socket, getopt, sys


(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:')

print('opciones: ', opt)

a = ""
p = ""
t = ""
j = ""

for (op, ar) in opt:
    if (op == '-a'):
        a = str(ar)
        print('Opcion -a exitosa!')
    elif (op == '-p'):
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


client_socket = socket.socket(socket.AF_INET, j)

host = ''
port = p

client_socket.connect((host, port))
while True:
    print('\nIngrese el mensaje: ')
    msg=''
    while True:
        try:
            msg += input() + '\n'
            if msg == '':
                break
        except EOFError:
            break


    client_socket.sendto(msg.encode('ascii'), (host, port))
