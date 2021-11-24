#!/usr/bin/python3
import socket
import time
import os
import subprocess
import signal
import asyncio


async def handle_client(client_conn, client_addr):
    
    loop = asyncio.get_event_loop()

    while True:
        msg = (await loop.sock_recv(client_conn, 255)).decode() # client_conn.recv(1024).decode()
        if not msg:
            break
        print('\nAddress: %s - Port: %d' % (client_addr[0], client_addr[1]))
        print('Recibido: %s' % msg)
        if ' ' in msg:
            cmd = msg.split(' ')
        else:
            cmd = msg
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE)
            output = 'OK\n%s' % result.stdout.decode()
            print('Result Message:\n%s' % output)
            await loop.sock_sendall(client_conn, output.encode())     #client_conn.sendto(output.encode(), (client_addr[0], client_addr[1]))
        except:
            await loop.sock_sendall(client_conn, 'ERROR\n'.encode()) #client_conn.sendto('ERROR\n'.encode(), (client_addr[0], client_addr[1]))
        await asyncio.sleep(1)
        
    client_conn.close()
    print('client disconnect')


async def run_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 9007
    server_socket.bind((host, port))
    server_socket.listen(5)
    server_socket.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        conn, addr = await loop.sock_accept(server_socket)
        loop.create_task(handle_client(conn, addr))

asyncio.run(run_server())
