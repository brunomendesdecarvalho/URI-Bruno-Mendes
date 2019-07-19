# coding: utf-8

l = list(range(1,101))
s = 0

while len(l) > 0:
    s += 1/l.pop(0)
print('%.2f' % s)