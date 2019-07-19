# coding: utf-8

from math import log
from decimal import Decimal

while True:
    try:
        N = int(input())
        print(Decimal(log(N,2)))
    except EOFError:
        break