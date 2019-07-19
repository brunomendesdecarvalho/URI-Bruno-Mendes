# coding: utf-8

N = int(input())
n1, n2, n3 = 1, 2, 3
while N > 0:
    print('%d %d %d PUM' % (n1, n2, n3))
    n1 += 4
    n2 += 4
    n3 += 4
    N -= 1