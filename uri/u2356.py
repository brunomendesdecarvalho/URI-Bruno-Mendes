# coding: utf-8

D = 0
S = 0

while True:
    try:
        D = input()
        S = input()

        if S in D:
            print('Resistente')
        else:
            print('Nao resistente')

    except EOFError:
        exit()