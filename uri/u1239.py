# coding: utf-8


def main():
    while True:
        try:
            texto = input()
            bloggo(texto)
        except EOFError:
            break


def bloggo(texto):
    asterisco = 0
    underline = 0
    novo_texto = ''
    for i in texto:
        if i == '*' and asterisco == 0:
            novo_texto += '<b>'
            asterisco += 1
        elif i == '*' and asterisco == 1:
            novo_texto += '</b>'
            asterisco = 0
        elif i == '_' and underline == 0:
            novo_texto += '<i>'
            underline += 1
        elif i == '_' and underline == 1:
            novo_texto += '</i>'
            underline = 0
        else:
            novo_texto += i

    print(novo_texto)


main()