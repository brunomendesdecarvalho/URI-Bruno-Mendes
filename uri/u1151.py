# coding: utf-8
from __future__ import print_function

fibonacci = [0, 1]

n = int(input())

while len(fibonacci) < n:
    a = len(fibonacci)
    fibonacci.append(fibonacci[a-1]+fibonacci[a-2])
    a += 1

print(" ".join([str(x) for x in fibonacci]))