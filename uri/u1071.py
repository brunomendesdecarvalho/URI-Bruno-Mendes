# coding: utf-8

X = int(input())
Y = int(input())

num = [min([X,Y]), max([X,Y])]
l = []
soma = 0

for i in range(num[0], num[1] + 1):
    if i%2 != 0:
        l.append(i)
    else:
        pass



if len(l) == 0:
    print(0)

else:
    soma = sum(l)

    if X in l:
        soma -= X
    if Y in l:
        soma -= Y

    print(soma)