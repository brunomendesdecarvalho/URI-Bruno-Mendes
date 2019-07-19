# coding: utf-8

# entradas:

numeros_pares = []
i = 0

# computações:

while i < 5:
    a = int(input())
    if a % 2 != 0:
        pass
    else:
        numeros_pares.append(a)

    i += 1

# saída:

print('%d valores pares' % len(numeros_pares))