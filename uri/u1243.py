# coding: utf-8


def main():
    while True:
        try:
            problema = input().split(' ')
            classificar_problema(problema)

        except EOFError:
            break


def classificar_problema(problema):
    media_palavras = 0
    num_palavras = 0
    for palavra in problema:
        if eh_palavra(palavra) == True:
            nova_palavra = ''
            for letra in palavra:
                if letra == '.':
                    continue
                else:
                    nova_palavra += letra

            media_palavras += len(nova_palavra)
            num_palavras += 1

        else:
            continue
    if num_palavras == 0:
        media_palavras = 0
    else:
        media_palavras = media_palavras // num_palavras

    if media_palavras <= 3:
        print(250)
    elif 4 == media_palavras or media_palavras == 5:
        print(500)
    elif media_palavras >= 6:
        print(1000)


def eh_palavra(palavra):
    nao_letra = 0
    for letra in palavra:
        if 46 <= ord(letra) <= 57:
            nao_letra += 1
        else:
            continue

    if nao_letra == 1:
        if '0123456789' in palavra:
            return False
        elif len(palavra) > 1 and palavra[len(palavra) - 1] == '.':
            return True
        else:
            return False

    elif nao_letra > 1:
        return False

    elif len(palavra) == 0:
        return False

    return True


main()