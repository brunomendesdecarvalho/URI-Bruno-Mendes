# coding: utf-8

N = int(input())
divisivel2 = 'a'
positivo = 'b'

while N > 0:
    numero = int(input())
    if numero == 0:
        print('NULL')
    else:

        if numero % 2 == 0:
            divisivel2 = 'EVEN'
        else:
            divisivel2 = 'ODD'

        if abs(numero) == numero:
            positivo = 'POSITIVE'
        else:
            positivo = 'NEGATIVE'

        print('%s %s' % (divisivel2, positivo))

    N -= 1