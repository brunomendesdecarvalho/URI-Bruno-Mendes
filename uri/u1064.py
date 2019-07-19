# coding: utf-8

# entradas:

numeros_positivos = []
i = 0

# computações:

while i < 6:
    a = float(input())
    if a < 0:
        pass
    else:
        numeros_positivos.append(a)

    i += 1

media = sum(numeros_positivos)/len(numeros_positivos)

# saídas:

print('%d valores positivos' % len(numeros_positivos))
print('%.1f' % media)