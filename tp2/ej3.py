#!/usr/bin/python3

import getopt, sys, os
import subprocess
from datetime import datetime


def option_reading():

    (opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')

    for (op, arg) in opt:
        if op in '-c':
            if " " in arg:
                command = arg.split()
            else:
                command = str(arg)

        elif op in '-f':
            output_file = str(arg)

        elif op in '-l':
            log_file = str(arg)

        else:
            print('comando no valido')

    return command, output_file, log_file

def main():

    command, output_file, log_file = option_reading()

    if not os.path.exists(output_file):
        output_file = open(output_file, 'w')
    else:
        output_file = open(output_file, 'a')

    if not os.path.exists(log_file):
        log_file = open(log_file, 'w')
    else:
        log_file = open(log_file, 'a')
    
    try:
        output_file.write(subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").strip())
        log = f'\n{datetime.now()}: Comando {command} ejecutado correctamente'
        log_file.write(log)
    except:
        log = f'Error al ejecutar el comando {command}'
        log_file.write(log)



main()