# coding: utf-8

# entradas:

A, B, C = input().split(" ")
A, B, C = float(A), float(B), float(C)

# saídas:

if A < B + C and B < A + C and C < A + B:
    print('Perimetro = %.1f' % (A + B + C))
else:
    print('Area = %.1f' % ((A+B)*C/2))