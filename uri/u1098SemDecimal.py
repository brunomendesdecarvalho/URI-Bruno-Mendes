# coding: utf-8

I = 0
J = 10
c = 1

while c <= 4 and I <= 20:
    c += 1

    if I%10 == 0:
            print('I=%d J=%d' % (I/10, J/10))

    else:
        print('I=%.1f J=%.1f' % (I/10, J/10))

    J += 10
    if c == 4:
        I += 2
        J = 10 + I
        c = 1