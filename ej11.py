# !/usr/bin/python3
from threading import Thread
from multiprocessing import Pipe
import os, sys, time


def child1(r):
    while True:
        time.sleep(0.5)
        print('leyendo mensaje: ')
        msg = input()
        r.send(msg)
    

def child2(w):
    while True:
        msg = w.recv()
        print('leyendo PID:', os.getpid(),': ',msg)

if __name__ == '__main__':
    print(os.getppid())
    a, b = Pipe()
    p1 = Thread(target= child1, args=(a,))
    p2 = Thread(target= child2, args=(b,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()