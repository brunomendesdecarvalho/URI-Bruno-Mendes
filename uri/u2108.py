# coding: utf-8


def main():
    maior_palavra = ''
    tamanho_maior_palavra = 0
    while True:
        string = input().split(" ")
        if string == ['0']:
            break
        else:
            maior_palavra, tamanho_maior_palavra = contar_caracteres(string, maior_palavra, tamanho_maior_palavra)
    print()
    print('The biggest word: %s' % maior_palavra)


def contar_caracteres(string, maior_palavra, tamanho_maior_palavra):
    tamanhos = []
    for i in string:
        tamanhos.append(str(len(i)))
        if len(i) >= tamanho_maior_palavra:
            tamanho_maior_palavra = len(i)
            maior_palavra = i

    nova_string = '-'.join(tamanhos)

    print(nova_string)
    return maior_palavra, tamanho_maior_palavra


main()