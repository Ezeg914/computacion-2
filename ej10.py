#!/usr/bin/python3

from multiprocessing import Process, Queue
import os, time

def childs():
    print('Proceso',n,', PID:',os.getpid())
    time.sleep(n)
    q.put(str(os.getpid())+'\\t')
    



if __name__ == '__main__':
    q = Queue()
    n= 0
    for _ in range(10):
        n = n+1
        p = Process(target=childs)
        p.start()
        p.join()
    for _ in range(n):
        print(q.get())

    
