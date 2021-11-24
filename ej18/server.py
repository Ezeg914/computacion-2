#!/usr/bin/python3
import socket, sys, getopt, os
from time import sleep
from threading import Thread, Lock

def child(lock, f, r, c):
    lock.acquire()
    try:
        with open(f,'a') as file:
            for _ in range(int(r)):
                file.write(c)
            file.close
    finally:
        lock.release()
        print('Finish thread!')

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:f:')

print('opciones: ', opt)


p = ""
f = ""



for (op, ar) in opt:
    if (op == '-p'):
        p = int(ar)
        print('Opcion -p exitosa!')
    elif (op == '-f'):
        f = str('tmp/' + ar)
        if not os.path.exists('./tmp'):
            os.makedirs('./tmp')
        print('Opcion -f exitosa!')
    else:
        print('Opcion incorrecta!')

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ""
port = p

server_socket.bind((host, port))
server_socket.listen(5)

stage = 0
lock = Lock()
while True:
    conn, addr = server_socket.accept()
    c = conn.recv(1024).decode('ascii')
    r = conn.recv(1024).decode('ascii')
    p = Thread(target=child, args = (lock,f,r,c))
    p.start()
    sleep(0.1)
    p.join()