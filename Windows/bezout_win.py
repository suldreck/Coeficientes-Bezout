#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#Script para Windows

import os
def bezout(a, b):

    if a == 0 and b == 0: return (0, 0, 1)
    if a == 0: return (abs(b), 0, b/abs(b))
    if b == 0: return (abs(a), a/abs(a), 0)
    x_sign = 1; y_sign = 1
    if a < 0: a = -a; x_sign = -1
    if b < 0: b = -b; y_sign = -1
    x = 1; y = 0; r = 0; s = 1
    while b != 0:
        (c, q) = (a%b, a/b)
        (a, b, r, s, x, y) = (b, c, x-q*r, y-q*s, r, s)
    return (a, x*x_sign, y*y_sign)

os.system("cls")
print "Programa que calcula el MCD de 2 numeros y halla los coeficientes de Bezout, dando despues la expresion integra"
print
raw_input('Pulse una tecla para continuar...')

salir=1
while salir == 1:
    os.system("cls")
    m=input("Introduzca un valor: ")
    n=input("Introduzca otro valor: ")
    if m>n:
        os.system("cls")
        sol=bezout(m,n)
        print "valor1=",m
        print "valor2=",n
        print "--------------------"
        print "MCD:",sol[0]
        print "Coef Bezout 1:",sol[1]
        print "Coef Bezout 2:",sol[2]
        print
        print
        print "Expresion --->",str(m)+"x("+str(sol[1])+")","+",str(n)+"x("+str(sol[2])+")","=",sol[0]
        print
        raw_input('Pulse una tecla para continuar...')
    elif m<n:
        os.system("cls")
        sol=bezout(n,m)
        print "valor1=",m
        print "valor2=",n
        print "--------------------"
        print "MCD:",sol[0]
        print "Coef Bezout 1:",sol[1]
        print "Coef Bezout 2:",sol[2]
        print
        print
	print "Expresion --->",str(m)+"x("+str(sol[1])+")","+",str(n)+"x("+str(sol[2])+")","=",sol[0]
        print
        raw_input('Pulse una tecla para continuar...')
    else:
        os.system("cls")
        print "He dicho que introduzca valores diferentes"
        print
        print
        raw_input('Pulse una tecla para continuar...')
    os.system("cls")
    salirpreg=raw_input("Desea salir (S/N): ")
    if salirpreg == "S" or salirpreg == "s":
        salir=0
