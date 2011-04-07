#!/usr/bin/python
# -*- coding: utf_8 -*-
# primos.py: calculo de la sucesion
from math import sqrt

def prim(n):
	"""Muestra los numeros primos existentes hasta el numero n
	@param n: se obtiene los numeros primos menores a n
	"""
	lista = [];
	if (n==1):
		print "No hay numeros primos menor o igual que 1"
	elif (n>1):
		#Se utiliza la idea de que todo natural es compuesto de primos
		#Se busca divisor de un numero n hasta sqrt(n)
		lista.append(2)
		for i in range(3,n+1):
			j=0
			primo = 1
			while (j<len(lista)) & (primo) & (lista[j]<=int(sqrt(i))):
				if (i%lista[j]==0):
					primo = 0
				j = j+1
			if (primo):
				lista.append(i)
		print "Lista de numeros primos menor o igual a "+str(n)+":"
		for k in range(len(lista)):
			print lista[k]
	else:
		print "Se requiere un numero natural y sea distinto a 0"

if (__name__ == "__main__"):
	import sys
	prim(int(sys.argv[1]))

				 
