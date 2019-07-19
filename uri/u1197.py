# coding: utf-8

while True:
    try:
        v, t = map(int, input().split(' '))
        desloc = v*(2*t)
        print(int(desloc))

    except EOFError:
        break