# coding: utf-8


def main():
    n = int(input())
    pecas = pecas_compradas()
    comprar_peca(n, pecas)


def pecas_compradas():
    vetor = list(map(int, input().split(' ')))
    return vetor


def comprar_peca(n, pecas):
    for i in range(1, n+1):
        if i in pecas:
            continue
        else:
            print(i)


main()
