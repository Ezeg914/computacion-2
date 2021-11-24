#!/usr/bin/python3
import socket
import time
import subprocess
from multiprocessing import Process

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 8005

server_socket.bind((host, port))
server_socket.listen(5)


def server(conn, addr):
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print('\nAddress: %s - Port: %d' % (addr[0], addr[1]))
        print('Recibido: %s' % msg)
        if ' ' in msg:
            cmd = msg.split(' ')
        else:
            cmd = msg
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE)
            output = 'OK\n%s' % result.stdout.decode()
            print('Result Message:\n%s' % output)
            conn.sendto(output.encode(), (addr[0], addr[1]))
        except:
            conn.sendto('ERROR\n'.encode(), (addr[0], addr[1]))
        time.sleep(1)

    conn.close()
    print('client disconnect')



while True:
    conn, addr = server_socket.accept()
    print("Tengo una conexión de", str(addr))
    p = Process(target=server, args=(conn, addr))
    p.start()