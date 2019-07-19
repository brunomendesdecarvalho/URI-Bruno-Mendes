# coding: utf-8


def main():
    n = int(input())
    while n > 0:
        print(is_prime(int(input())))
        n -= 1


def is_prime(number):
    from math import sqrt

    root = int(sqrt(number))
    for d in range(2, root + 1):
        if number % d == 0:
            return 'Not Prime'

    return 'Prime'


main()