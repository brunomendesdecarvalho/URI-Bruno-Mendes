# coding: utf-8

n = 0
nota1 = 0
nota2 = 0

while n < 2:

    while nota1 == 0:

        nota1 = float(input())

        if nota1 < 0 or nota1 > 10:

            print('nota invalida')
            nota1 = 0

        else:
               n += 1

    while nota2 == 0:

        nota2 = float(input())

        if nota2 < 0 or nota2 > 10:

            print('nota invalida')
            nota2 = 0

        else:
            n += 1

print('media = %.2f' % ((nota1 + nota2) / 2))