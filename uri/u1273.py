# coding: utf-8


def main():
    primeira_vez = True
    while True:
        strings = []
        n = int(input())
        if n == 0:
            break
        else:
            if primeira_vez == False:
                print()
            for i in range(n):
                strings.append(input())
            maior_string = maior(strings)
            justificar(strings, maior_string)
        primeira_vez = False

def maior(strings):
    maior_string = ''
    for palavra in strings:
        if len(palavra) > len(maior_string):
            maior_string = palavra

    return maior_string


def justificar(strings, maior_string):
    for i in strings:
        print(((len(maior_string) - len(i)) * ' ') + i)


main()