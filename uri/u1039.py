# coding: utf-8

from math import sqrt

def distancia_centros(x1, y1, x2, y2):

    d = sqrt((x1-x2)**2+(y1-y2)**2)

    return d

def contida(d, r1, r2):

    if d == 0:

        if r2 <= r1:
            estado = 'RICO'
        else:
            estado = 'MORTO'

    elif d <= r1-r2:

        estado = 'RICO'

    else:

        estado = 'MORTO'

    return estado

while True:
    try:
        r1,x1,y1,r2,x2,y2 = map(int, input().split(" "))
        d = distancia_centros(x1, y1, x2, y2)
        estado = contida(d, r1, r2)
        print(estado)

    except EOFError:
        break