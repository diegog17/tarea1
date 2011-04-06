#!/usr/bin/python
# -*- coding: utf_8 -*-
# fibonacci.py: calculo de la sucesion
def fib(n):
	""" Calcula la sucesion de Fibonacci
	@param n: paso hasta donde se calcula la sucesion
	"""
	a, b = 0, 1
	for i in range(n+1):
		print "fib("+str(i)+")="+str(b)+"\n"
		a, b = b, a + b
					
if (__name__ == "__main__"):
	import sys
	fib(int(sys.argv[1]))
	
