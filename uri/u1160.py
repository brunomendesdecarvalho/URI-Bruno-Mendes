# coding: utf-8

from math import trunc

casos = int(input())
cresc_A, cresc_B, tempo = 0, 0, 0

while casos > 0:
    casos -= 1
    dados = list(input().split(' '))
    PA, PB, G1, G2 = int(dados[0]), int(dados[1]), float(dados[2]), float(dados[3])

    while PA <= PB:

        cresc_A = trunc(PA*(G1/100))
        cresc_B = trunc(PB*(G2/100))

        PA += cresc_A
        PB += cresc_B

        tempo += 1
        if tempo > 100:
            print('Mais de 1 seculo.')
            break


        if PA > PB:
            print('%d anos.' % tempo)
            break

    tempo = 0