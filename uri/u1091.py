# coding: utf-8

entrada = 1
aux = 0

while entrada > 0:
    aux = 0
    entrada = int(input())

    if entrada == 0:
        exit()

    else:
        N, M = map(int, input().split(' '))

        while aux < entrada:
            X, Y = map(int, input().split(' '))

            if X == N or Y == M:
                print('divisa')

            elif X > N and Y > M:
                print('NE')

            elif X < N and Y > M:
                print('NO')

            elif X < N and Y < M:
                print('SO')

            elif X > N and Y < M:
                print('SE')

            aux += 1