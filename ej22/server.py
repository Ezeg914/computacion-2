#!/usr/bin/python3
import socket, sys, time, getopt, os
from multiprocessing import Process
from tasks import *

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')

print('opciones: ', opt)

h = ""
p = ""


for (op, ar) in opt:
    if (op == '-h'):
        h = str(ar)
        print('Opcion -h exitosa!')
    elif (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    else:
        print('Opcion incorrecta')

        


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = h
port = p

server_socket.bind((host, port))
server_socket.listen(5)

def server(conn, addr):
    operacion = conn.recv(1024).decode('ascii')
    num1 = (conn.recv(1024).decode('ascii'))
    num2 = (conn.recv(1024).decode('ascii'))
    print (operacion, num1, num2)
    if operacion == "suma":
        res = suma.delay(num1,num2)
    elif operacion == "resta":
        res = resta.delay(num1,num2)
    elif operacion == "multi":
        res = multi.delay(num1,num2)
    elif operacion == "div":
        res = div.delay(num1,num2)
    elif operacion == "pot":
        res = pot.delay(num1,num2)
        
    data = res.get(timeout=10)
    conn.sendto(data.encode('ascii'),(addr[0], addr[1]))
    conn.close()
    
while True:
    conn, addr = server_socket.accept()
    print("Tengo una conexión de", str(addr))
    p = Process(target=server, args=(conn,addr))
    p.start()
    