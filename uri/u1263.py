# coding: utf-8


def main():
    while True:
        try:
            frase = input().split(" ")
            verificar_aliteracao(frase)

        except EOFError:
            break


def verificar_aliteracao(frase):
    cont = 0
    letra = ''
    aliterada = ''
    for palavra in frase:
        if palavra[0].lower() == aliterada:
            continue
        elif palavra[0].lower() == letra.lower():
            cont += 1
            aliterada = palavra[0].lower()
        else:
            letra = palavra[0].lower()
            aliterada = ''
            pass

    print(cont)


main()