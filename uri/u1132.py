# coding: utf-8

X = int(input())
Y = int(input())
limites = [X, Y]
limites.sort()
l = []

for i in range(limites[0], limites[1] + 1):
    if i%13 != 0:
        l.append(i)
    else: pass

print(sum(l))