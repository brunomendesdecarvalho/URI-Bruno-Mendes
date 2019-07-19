# coding: utf-8

novo_calculo = 's'

while novo_calculo == 's':
    a = 3
    media = 0
    nota = 0
    n = 0

    while n < 2:

        nota = float(input())
        if 0 <= nota <= 10:
            n += 1
            media += nota
        else:
            print('nota invalida')

    print('media = %.2f' % (media / 2))

    while (a != 1 and a != 2):

        a = int(input('novo calculo (1-sim 2-nao)\n'))

        if a == 1:
            novo_calculo = 's'

        elif a == 2:
            novo_calculo = 'n'

        else:
            a = int(input('novo calculo (1-sim 2-nao)\n'))