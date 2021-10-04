#!/usr/bin/python3
# ----------------------------------------------
# command-line: python3 ej17.py -n 26 -f hola.txt -r 5
# ----------------------------------------------
from multiprocessing import Process, Lock
import getopt, sys, os

def child(lock, f, r, stage):
    lock.acquire()
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    try:
        with open(f,'a') as file:
            if stage == 0:
                file.truncate(0)
            for _ in range(r):
                file.write(alphabet[stage])
    finally:
        lock.release()

if __name__ == '__main__':

    (opt, arg) = getopt.getopt(sys.argv[1:], 'n:r:f:')

    print('opciones: ', opt)

    n = ""
    r = ""
    f = ""

    for (op, ar) in opt:
        if (op == '-n'):
            n = int(ar)
            print('Opcion -n exitosa!')
        elif (op == '-r'):
            r = int(ar)
            print('Opcion -r exitosa!')
        elif (op == '-f'):
            f = str('tmp/' + ar)
            if not os.path.exists('./tmp'):
                os.makedirs('./tmp')
            print('Opcion -f exitosa!')
        else:
            print('Opcion incorrecta!')

    stage = 0
    lock = Lock()
    for _ in range(n):
        p = Process(target=child, args = (lock,f,r, stage))
        stage += 1
        p.start()
        p.join()