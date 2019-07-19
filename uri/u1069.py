# coding: utf-8

n = int(input())

for i in range(n):
    areia = input()
    diamantes = 0
    inicio = 0

    for j in range(len(areia)):
        if (areia[j] == "<"):
            inicio += 1
        if (areia [j] == ">" and inicio > 0):
            diamantes += 1
            inicio -= 1

    print(diamantes)