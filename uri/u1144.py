# coding: utf-8

N = int(input())
n1, n2, n3 = 1, 0, 0

while N > 0:
    n2 = n1 ** 2
    n3 = n1 ** 3
    print('%d %d %d' % (n1, n2, n3))
    n2 += 1
    n3 += 1
    print('%d %d %d' % (n1, n2, n3))
    n1 += 1
    N -= 1