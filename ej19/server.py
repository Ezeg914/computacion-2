#!/usr/bin/python3
import socket
import time
import subprocess
from multiprocessing import Process
import socketserver
import threading, os, sys

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            msg = self.request.recv(1024).decode()
            if not msg:
                break
            print('Recibido: %s' % msg)
            if ' ' in msg:
                cmd = msg.split(' ')
            else:
                cmd = msg
            try:
                result = subprocess.run(cmd, stdout=subprocess.PIPE)
                output = 'OK\n%s' % result.stdout.decode()
                print("server")
                print('Result Message:\n%s' % output)
                self.request.send(output.encode())
            except:
                self.request.send('ERROR\n'.encode())
            time.sleep(1)

        self.request.close()
        print('client disconnect')

class ThreadedServer(socketserver.ThreadingMixIn,socketserver.TCPServer,):
    pass

class ForkingServer(socketserver.ForkingMixIn,socketserver.TCPServer,):
    pass


if __name__ == '__main__':
    import socket
    import threading, getopt
    
    (opt, arg) = getopt.getopt(sys.argv[1:], 'm:')

    print('opciones: ', opt)

    m = ""


    for (op, ar) in opt:
        if (op == '-m'):
            m = str(ar)
            if m == "t":
                j = ThreadedServer
                print('Opcion -m ThreadedServer exitosa!')
            elif m == "p":
                j = ForkingServer
                print('Opcion -m ForkingServer exitosa!')
            else:
                print('Opcion incorrecta')
                
                
                
    address = ('localhost', 0)
    server = j(address,MyTCPHandler)
    host, port = server.server_address 

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  
    t.start()

    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        msg = input('> ').encode()
        try:
            client_socket.sendto(msg, (host, port))
        except socket.error:
            print('Error Code: ' + str(msg[0]) + 'Message' + msg[1])
            sys.exit()
        print("client\n",client_socket.recv(1024).decode())


