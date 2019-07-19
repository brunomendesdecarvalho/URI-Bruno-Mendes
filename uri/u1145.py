# coding: utf-8

x, y = map(int, input().split(' '))
contador = 1
lista = list(range(1, y+1))

while contador <= x:
    if contador < x:
        print(lista.pop(0), end=' ')
    elif contador == x:
        if lista[0] == y:
            print(lista.pop(0))
            exit()
        else:
            print(lista.pop(0))
            contador = 0
    contador += 1