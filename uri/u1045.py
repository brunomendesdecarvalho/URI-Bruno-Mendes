# coding: utf-8

lados = list(float(i) for i in input().split(" "))

lados = sorted(lados,key=float , reverse=True)

A = lados.pop(0)
B = lados.pop(0)
C = lados.pop(0)

if (A >= B + C):
    print('NAO FORMA TRIANGULO')
    exit()
if(A**2 == B**2 + C**2):
    print('TRIANGULO RETANGULO')
if(A**2 > B**2 + C**2):
    print('TRIANGULO OBTUSANGULO')
if(A**2 < B**2 + C**2):
    print('TRIANGULO ACUTANGULO')
if(A == B and A == C):
    print('TRIANGULO EQUILATERO')
if(A == B and A != C or  B == C and B != A):
    print('TRIANGULO ISOSCELES')