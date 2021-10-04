# !/usr/bin/python3

from multiprocessing import Process, Pipe
import os, sys, time


def child1(r):
    sys.stdin = open(0)
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
    a, b = Pipe()
    print(os.getppid())
    p1 = Process(target= child1, args=(a,))
    p2 = Process(target= child2, args=(b,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()