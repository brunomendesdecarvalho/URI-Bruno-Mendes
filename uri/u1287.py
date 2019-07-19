# coding: utf-8


def main():
    while True:
        try:
            string = input()
            numero = processar(string)
            avaliar_inteiro(numero)
        except EOFError:
            break


def processar(string):
    nova_string = ''
    for i in string:
        if i == 'l':
            nova_string += '1'
        elif i == 'o' or i == 'O':
            nova_string += '0'
        elif i in '0123456789':
            nova_string += i
        elif i == ',' or i == ' ':
            continue
        else:
            return ''

    return nova_string


def avaliar_inteiro(numero):
    if numero == '' or int(numero) > 2147483647:
            print('error')
    else:
        print(int(numero))


main()