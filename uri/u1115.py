# coding: utf-8

X, Y = 1, 1

while True:

    X, Y = map(int, input().split(' '))

    if X > 0:

        if Y > 0:
            print('primeiro')

        elif Y < 0:
            print('quarto')

    elif X < 0:

        if Y > 0:
            print('segundo')

        elif Y < 0:
            print('terceiro')

    if X == 0 or Y == 0:
        break