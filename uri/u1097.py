# coding: utf-8

I = 1
J = 7
c = 1

while I <= 9 and c <= 3:

    print('I=%d J=%d' % (I, J))
    J -= 1
    c += 1

    if c > 3:
        I += 2
        J += 5
        c = 1