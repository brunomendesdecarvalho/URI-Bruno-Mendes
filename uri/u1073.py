# coding: utf-8

N = int(input())
l = []

for i in range(1, N+1):
    if i%2 == 0:
        l.append(i)
    else: pass

while len(l) > 0:
    num = l.pop(0)
    print('%d^2 = %d' % (num, num**2))