# coding: utf-8

C = int(input())

while C > 0:
    C -= 1
    nome, forca = input().split(' ')

    if nome == 'Thor':
        print('Y')
    else:
        print('N')