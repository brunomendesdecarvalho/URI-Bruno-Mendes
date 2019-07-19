# coding: utf-8

n = int(input())
i = 0
nome = 'A'
while i < n:
    i += 1
    nome = input()
    if nome != 'Batmain':
        print('Y')
    else:
        print('N')
