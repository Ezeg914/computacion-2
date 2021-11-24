import socket
import getopt
import sys


(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')

print('opciones: ', opt)

h = ""
p = ""

for (op, ar) in opt:
    if (op == '-h'):
        a = str(ar)
        print('Opcion -h exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    else:
        print('Opcion incorrecta!')
# Protocolo TCP (socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = h
port = p

client_socket.connect((host, port))

while True:
    msg = input('Ingrese msg: ').encode('ascii')
    try:
        client_socket.sendto(msg, (host, port))
    except socket.error:
        print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()
sys.exit()