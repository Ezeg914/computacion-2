#!/usr/bin/python3

import getopt
import sys

(opt,arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')

print("opciones: ", opt)


operator = ''
num1 = ''
num2 = ''

for (op, ar) in opt:
	if (op == '-o'):
		print("operator =", ar)
		operator = ar
	elif (op == '-n'):
		print("number 1 =", ar)
		num1 = int(ar)
	elif (op == '-m'):
		print("number 2 =", ar)
		num2 = int(ar)
		
		if (operator == '+'):
			print('El resultado nos da: %d + %d = %d' % (num2, num1, num2 + num1))
		elif (operator == '-'):
			print('El resultado nos da: %d - %d = %d' % (num2, num1, num2 - num1))
		elif (operator == '*'):
			print('El resultado nos da: %d * %d = %d' % (num2, num1, num2 * num1))
		elif (operator == '/'):
			print('El resultado nos da: %d / %d = %d' % (num2, num1, num2 / num1))

	else:
		print("Opcion invalida")
