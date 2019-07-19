# coding: utf-8

N = 0
maior = 0
posicao = 0

while N < 100:
    num = int(input())
    N += 1
    if num > maior:
        maior = num
        posicao = N

print(maior)
print(posicao)