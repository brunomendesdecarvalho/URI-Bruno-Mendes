# coding: utf-8

T = int(input())
i = 0
vazias = 0

while(i < T):
    i += 1
    N, K = input().split(' ')
    N, K = int(N), int(K)

    if (N >= K):
        vazias = N%K + (N//K)
    elif(N < K):
        vazias = N
    print(vazias)