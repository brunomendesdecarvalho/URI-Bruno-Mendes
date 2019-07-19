# coding: utf-8

# entradas:

numeros_pares = []
numeros_impares = []
numeros_positivos = []
numeros_negativos = []
i = 0

# computações:

while i < 5:
    a = int(input())

    if a % 2 != 0:
        numeros_impares.append(a)
    else:
        numeros_pares.append(a)
    if a < 0:
        numeros_negativos.append(a)
    elif a > 0:
        numeros_positivos.append(a)

    i += 1

# saída:

print('%d valor(es) par(es)' % len(numeros_pares))
print('%d valor(es) impar(es)' % len(numeros_impares))
print('%d valor(es) positivo(s)' % len(numeros_positivos))
print('%d valor(es) negativo(s)' % len(numeros_negativos))