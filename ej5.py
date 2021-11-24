"""
Realice un programa que genere N procesos hijos. Cada proceso al iniciar deberá mostrar:
“Soy el proceso N, mi padre es M” N será el PID de cada hijo, y M el PID del padre.

              padre
            /   |   \.
       hijo1  hijo2  hijo3

La cantidad de procesos hijos N será pasada mediante el argumento "-n" de línea de comandos.
"""

#!/usr/bin/python3

import os, getopt, sys


(opt, arg) = getopt.getopt(sys.argv[1:], 'n:')

num = ''

for (op, ar) in opt:
    if (op == '-n'):
        num = int(ar)

def child(x):
    print("Soy el proceso %d, mi padre es %d" % (os.getpid(), x))
    os._exit(0)

def parent():
    pid = os.getpid()

    for x in range(num):
        child2 = os.fork()
        if child2 == 0:
            child(pid)

parent()