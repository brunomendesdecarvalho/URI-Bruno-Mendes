# coding: utf-8

n1 = 0
n2 = 1
count = 2
i = 0
fibonacci = []
fibonacci.append(n1)
fibonacci.append(n2)

T = int(input())

while i < T:
    i += 1
    N = int(input())

    while count <= N:
        num = fibonacci[count-1] + fibonacci[count-2]
        fibonacci.append(num)
        count += 1

    print('Fib(%d) = %d' % (N, fibonacci[N]))