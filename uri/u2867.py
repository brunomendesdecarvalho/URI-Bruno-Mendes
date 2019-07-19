# coding: utf-8

C = int(input())
digitos = 0
i = 0

while i < C:

    N, M = map(int, input().split(' '))
    potencia = str(N**M)
    print(len(potencia))
    i += 1