# coding: utf-8

X = int(input())
Y = int(input())

numeros = [X, Y]
numeros.sort()

for i in range(numeros[0]+1, numeros[1]):
    if i%5 == 2 or i%5 == 3:
        print(i)