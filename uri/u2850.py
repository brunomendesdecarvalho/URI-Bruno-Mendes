# coding: utf-8

while True:
    try:
        perna = input()

        if perna =='esquerda':
            print('ingles')

        elif perna =='direita':
            print('frances')

        elif perna =='nenhuma':
            print('portugues')

        elif perna =='as duas':
            print('caiu')

    except EOFError:
        break