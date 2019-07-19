# coding: utf-8

while True:
    try:
        T = int(input())
        tempos = []

        while T > 0:
            T -= 1
            tempos.append(float(input()))

        print(min(tempos))

    except EOFError:
        break