# coding: utf-8


def main():
    a = int(input())
    for i in range(0, 10):
        print('N[%d] = %d' % (i, a))
        a *= 2


main()