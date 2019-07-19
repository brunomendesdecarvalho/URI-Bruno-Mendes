# coding: utf-8
from decimal import Decimal

I = 0
J = 1
c = 1

while c <= 4 and I <= 2:
    c += 1
    if I%1 == 0:
            print('I=%.f J=%.f' % (I, J))
    else:
        print('I=%.1f J=%.1f' % (I, J))

    J += 1
    if c == 4:
        I += Decimal('0.2')
        J = 1 + I
        c = 1