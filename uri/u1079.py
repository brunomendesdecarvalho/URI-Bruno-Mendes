# coding: utf-8

N = int(input())
media = 0.0

while N > 0:

    num1, num2, num3 = map(float, input().split(' '))
    media = (num1*2 + num2*3 + num3*5)/10
    print('%.1f' % media)
    N -= 1