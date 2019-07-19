# coding: utf-8


def main():
    while True:
        try:
            senha = input()
            if (6 <= len(senha) <= 32) and verificar_maiuscula(senha) == True and\
                verificar_minuscula(senha) == True and\
                verificar_numero(senha) == True and \
                verificar_simbolo(senha) == False:

                print('Senha valida.')
            else:
                print('Senha invalida.')

        except EOFError:
            break


def verificar_maiuscula(senha):
    for i in senha:
        if 65 <= ord(i) <= 90:
            return True
        else:
            continue

    return False


def verificar_minuscula(senha):
    for i in senha:
        if 97 <= ord(i) <= 122:
            return True
        else:
            continue

    return False


def verificar_numero(senha):
    for i in senha:
        if i in '0123456789':
            return True
        else:
            continue

    return False


def verificar_simbolo(senha):
    for i in senha:
        if 0 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 127:
            return True
        else:
            continue

    return False


main()