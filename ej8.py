# !/usr/bin/python3

import time, signal, os


def handler(signum, frame):
    return


if __name__ == '__main__':
    procesoA = os.getpid()
    a, b = os.pipe()
    signal.signal(signal.SIGUSR1, handler)
    print("A (PID = %s) leyendo:" % os.getpid())
    procesoB = os.fork()

    if not procesoB:
        procesoC = os.fork()

    if os.getpid() == procesoA:
        time.sleep(0.1)
        os.close(b)
        pipea = os.fdopen(a)
        os.kill(procesoB, signal.SIGUSR1)
        signal.pause()
        print(pipea.read())

    elif not procesoB and procesoC:
        signal.pause()
        os.close(a)
        pipe_b = os.fdopen(b, 'w')
        pipe_b.write("Mensaje 1 (PID = %d)" % os.getpid())
        os.kill(procesoC, signal.SIGUSR1)

    else:
        signal.pause()
        os.close(a)
        pipe_a = os.fdopen(b, 'w')
        pipe_a.write("\nMensaje 2 (PID = %d)" % os.getpid())
        os.kill(procesoA, signal.SIGUSR1)

