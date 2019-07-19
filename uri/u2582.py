# # coding: utf-8
#
# musicas = ['PROXICITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']
#
# C = int(input())
#
# while C > 0:
#     C -= 1
#     X, Y = map(int, input().split(' '))
#     print(musicas[X+Y])

C = int(input())

for i in range(C):
    X = input()
    X = X.split(' ')
    a = int(X[0]) + int(X[1])

    if a == 0:
        print('PROXYCITY')
    elif a == 1:
        print('P.Y.N.G.')
    elif a == 2:
        print('DNSUEY!')
    elif a == 3:
        print('SERVERS')
    elif a == 4:
        print('HOST!')
    elif a == 5:
        print('CRIPTONIZE')
    elif a == 6:
        print('OFFLINE DAY')
    elif a == 7:
        print('SALT')
    elif a == 8:
        print('ANSWER!')
    elif a == 9:
        print('RAR?')
    elif a == 10:
        print('WIFI ANTENNAS')