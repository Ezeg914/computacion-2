# !/usr/bin/python3

import os, time, signal 


def handler_child2(signal, frame):
    print("Soy el hijo2 con PID:", os.getpid(), "PONG")

def handler(signal, frame):
    pass

def sig(pid):
    os.kill(pid, signal.SIGUSR1)

if __name__ == '__main__':
    signal.signal(signal.SIGUSR1, handler)
    pid1 = os.fork()
    if pid1:
        pid2 = os.fork()
        if pid2:
            while True:
                signal.pause()
                sig(pid2)
        else:
            signal.signal(signal.SIGUSR1, handler_child2)
            while True:
                signal.pause()
    else:
        for i in range(3):
            ppid = os.getppid()
            sig(ppid)
            print("Soy el hijo1 con PID:", os.getpid(), "PING")
            time.sleep(5)
        print('\n')
        os.kill(pid1, signal.SIGTERM)
