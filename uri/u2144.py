# coding: utf-8

w1 = 1
w2 = 1
r = 1
medias = []

while w1 > 0 and w2 > 0 and r > 0:
    w1, w2, r = map(int, input().split(' '))

    if w1 == 0 and w2 == 0 and r == 0:
        break
    else:
        m = ((w1 * (1 + (r/30))) + (w2 * (1 + (r/30)))) / 2
        medias.append(m)

        if 1 <= m < 13:
            print('Nao vai da nao')

        if 13 <= m < 14:
            print('E 13')

        if 14 <= m < 40:
            print('Bora, hora do show! BIIR!')

        if 40 <= m <= 60:
            print('Ta saindo da jaula o monstro!')

        if m > 60:
            print('AQUI E BODYBUILDER!!')

if sum(medias) / len(medias) > 40:
    print()
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')