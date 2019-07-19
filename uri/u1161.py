# coding: utf-8
from math import factorial
M = 0
N = 0

while True:
    try:
        M,N = map(int, input().split())
        soma = factorial(M) + factorial(N)
        print(soma)
    except EOFError:
        break