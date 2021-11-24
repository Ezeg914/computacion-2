"""
Escribir un programa que en ejecución genere dos procesos, uno padre y otro hijo.
El hijo debe escribir "Soy el hijo, PID YYYY" 5 veces (YYYY es el pid del hijo).
El padre debe escribir "Soy el padre, PID XXXX, mi hijo es YYYY" 2 veces (XXXX es el pid del padre).
El padre debe esperar a que termine el hijo y mostrar el mensaje "Mi proceso hijo, PID YYYY, terminó".
El hijo al terminar debe mostrar "PID YYYY terminando".
"""

#!/usr/bin/python3

import os, time

def slowType(text, speed, newLine = True):
        for i in text:
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine:
            print()



def child():
    for x in range(5):
        slowType("Soy el hijo, PID %d" % (os.getpid()), .03)
    os._exit(0)

def dad():
    childProc = os.fork()
    if childProc == 0:
        child()
    else:
        childExit = os.wait()
        slowType("PID %d terminando" %(childExit[0]), .03)
        slowType("Mi proceso hijo, PID %d, terminó" % (childExit[0]), .03)
        for x in range(2):
            print("Soy el padre, PID %d, mi hijo es" % (os.getpid()),"%d"% (childExit[0]))

dad()
