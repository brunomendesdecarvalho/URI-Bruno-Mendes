# coding: utf-8

N = int(input())
l = []
i = 0

while i < 10000:
    if i % N == 2:
        l.append(i)
    else:
        pass
    i += 1

if len(l) > 0:
    while len(l) > 0:
        print(l.pop(0))