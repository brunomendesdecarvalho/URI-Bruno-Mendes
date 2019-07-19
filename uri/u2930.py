# coding: utf-8

E, D = input().split(" ")
E, D = int(E), int(D)

if(E > D or D >= 25):
    print('Eu odeio a professora!')

elif (D - E >= 3):
    print('Muito bem! Apresenta antes do Natal!')

elif(D - E < 3):
    print('Parece o trabalho do meu filho!')
    if(D + 2 > 24):
        print('Fail! Entao eh nataaaaal!')
    elif(D + 2 <= 24):
        print('TCC Apresentado!')
