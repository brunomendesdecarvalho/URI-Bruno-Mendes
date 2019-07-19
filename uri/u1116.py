# coding: utf-8

N = int(input())

while N > 0:
    x, y = map(int, input().split(' '))
    if y == 0:
        print('divisao impossivel')
    else:
        print('%.1f' % (x/y))

    N -= 1