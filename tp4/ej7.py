# !/usr/bin/python3

import os, time, signal,getopt, sys

def seg(pid):
    os .kill(pid, signal.SIGUSR2)

def handler(signal, frame):
    print('Soy el PID:',os.getpid(),', recibí la señal:',signal,'de mi padre PID:',os.getppid())

if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process='])

    for (op, ar) in opt:
        if (op == "-p" or op == "--process"):
            childs = int(ar)
            for x in range(childs):
                pid1 = os.fork()
                if pid1:
                    time.sleep(1)
                    print('Creando proceso:' ,pid1)
                    seg(pid1)
                    os.wait()
                else:
                    signal.signal(signal.SIGUSR2, handler)
                    signal.pause()
                    exit(0)

