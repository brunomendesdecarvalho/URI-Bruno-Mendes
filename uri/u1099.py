# coding: utf-8

N = int(input())
impares = []

while N > 0:
    inteiros = list(map(int, input().split(' ')))
    inteiros = sorted(inteiros)

    for i in range(inteiros[0], inteiros[1]):
        if i%2 != 0 and i == inteiros[0]:
            pass
        elif i%2 != 0:
            impares.append(i)
        else:
            pass

    print(sum(impares))

    N -= 1
    impares.clear()