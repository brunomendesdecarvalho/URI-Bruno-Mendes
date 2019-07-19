# coding: utf-8

while True:
    try:
        l = []
        n = int(input())
        while n > 0:
            l.append(input())
            n -= 1
        l = sorted(l)
        while len(l) > 0:
            print(l.pop(0))


    except EOFError:
        break