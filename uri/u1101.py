# coding: utf-8

while True:

    M, N = map(int, input().split(' '))

    if N <= 0 or M <= 0:
        break

    else:
        M, N = sorted([M, N])
        conjunto = list(range(M, N+1))
        soma = sum(conjunto)

        for i in conjunto:
            print('%d' % i, end=' ')
        print('Sum=%d' % soma)