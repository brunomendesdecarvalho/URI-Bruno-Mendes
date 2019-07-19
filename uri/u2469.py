# coding: utf-8

alunos = int(input())
notas = list(map(int, input().split(' ')))
notas = sorted(notas)
frequencia1 = 0 # frequencia modal
frequencia2 = 0 # frequencia do número i
moda = 0

for i in notas:
    if frequencia1 == 0 and frequencia2 == 0 and moda == 0:
        moda = i
        frequencia1 = notas.count(i)

    elif i == moda:
        pass

    else:
        frequencia2 = notas.count(i)

        if frequencia2 == frequencia1:
            if i > moda:
                moda = i

            else:
                pass

        elif frequencia2 > frequencia1:
            moda = i
            frequencia1 = frequencia2

print(moda)