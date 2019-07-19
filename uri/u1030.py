# coding: utf-8

# entradas:

NC = int(input())
i, n, k, remover = 0, 0, 0, 0
l = []

while (i < NC):
    remover = 0
    i += 1
    n, k = [int(a) for a in input().split(" ")]

# computações

    l = list(range(1, (n+1)))
    while (len(l) > 1):
        remover += (k - 1)
        while (remover >= n):
            remover -= n
        del l[remover]
        n -= 1
# saída

    print('Case %d: %d' % (i, l.pop(0)))

