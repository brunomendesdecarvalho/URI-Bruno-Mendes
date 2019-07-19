# coding: utf-8


def main():
    nome = input()
    nome = tudo_para_minuscula(nome)
    is_link_bolado(nome)


def tudo_para_minuscula(nome):
    return nome.lower()


def is_link_bolado(nome):
    if 'zelda' in nome:
        print('Link Bolado')
    else:
        print('Link Tranquilo')


main()