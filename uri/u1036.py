#coding: utf-8

import math

a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

delta = math.pow(b,2)-(4*a*c)

if (delta < 0 or a==0):
    print('Impossivel calcular')
else:
    delta = math.sqrt(delta)
    R1 = (-b+delta)/(2*a)
    R2 = (-b-delta)/(2*a)
    print('R1 = %.5f' %R1)
    print('R2 = %.5f' %R2)