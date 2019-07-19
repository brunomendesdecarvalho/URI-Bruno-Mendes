# coding: utf-8


def main():
    while True:
        d, n = input().split(' ')
        if d == '0' and n == '0':
            break
        else:
            falha(d, n)


def falha(d, n):
    novo_n = ''
    for i in n:
        if i == d:
            continue
        else:
            novo_n += i

    if novo_n == '':
        print(0)
    else:
        print(int(novo_n))


main()