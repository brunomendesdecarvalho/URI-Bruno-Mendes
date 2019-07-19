# coding: utf-8

X, Y = 0, 1

while X != Y:
    X, Y = map(int, input().split(' '))
    if X > Y:
        print('Decrescente')
    elif X < Y:
        print('Crescente')