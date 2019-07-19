# coding: utf-8

frase = input().split(' ')
frase_nova = ''
contador = 0
contador2 = 0
for palavra in frase:

    for letra in palavra:

        if letra == 'p' and contador%2 == 0:
            pass

        else:
            frase_nova += letra

        contador += 1

        if contador == len(palavra) and contador2 < len(frase)-1:
            frase_nova += ' '
            contador = 0

        elif contador2 == len(frase)-1:
            pass

    contador2 += 1

print(frase_nova)