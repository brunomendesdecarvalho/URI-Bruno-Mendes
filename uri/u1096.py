# coding: utf-8

I = 1
J = 7

while I <= 9 and J >= 5:
    print('I=%d J=%d' % (I, J))
    J -= 1
    if J < 5:
        I += 2
        J = 7
