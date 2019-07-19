# coding: utf-8

X = int(input())

l = []

while len(l) < 6:
    X += 1
    if X%2 != 0: l.append(X)
    else: pass

while len(l) > 0:
    print(l.pop(0))