# coding: utf-8

N = int(input())
In = []
Out = []
i = 0

while i < N:
    X = int(input())

    if X in range (10,21):
        In.append(X)
    else:
        Out.append(X)

    i += 1


print('%d in' % (len(In)))
print('%d out' % (len(Out)))