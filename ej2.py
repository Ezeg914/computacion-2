#!/usr/bin/python3

import getopt
import sys
import os.path

(opt,arg) = getopt.getopt(sys.argv[1:], 'i:o:')

print("opciones: ", opt)


file1 = ''
file2 = ''

for (op, ar) in opt:
	if (op == '-i'):
		file1 = str(ar)
		print("Original =",ar)

	elif (op == '-o'):
		file2 = str(ar)
		print("Copia =",ar)

		if os.path.isfile(file1):
			file1 = open(file1, 'r')
			file2 = open(file2, '+w')
			texto = file1.readlines()
			file2.write(str(texto))
			print("se copio exitosamente")
		else:
			print("el archivo no existe")
	else:
		print("Opcion invalida")