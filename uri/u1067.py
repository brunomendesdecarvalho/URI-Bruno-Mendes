# coding: utf-8

X = int(input())
l = []

for i in range(1, X+1):
    if i%2 != 0:
        l.append(i)
    else:
        pass

while len(l) > 0:
    print(l.pop(0))