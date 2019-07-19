# coding: utf-8


def main():
    pares = []
    impares = []
    cont_par = 0
    cont_impar = 0
    for i in range(0, 15):
        numero = int(input())
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

        if len(pares) == 5:
            for par in pares:
                print('par[%d] = %d' % (cont_par, par))
                cont_par += 1
            pares = []
            cont_par = 0
        if len(impares) == 5:
            for impar in impares:
                print('impar[%d] = %d' % (cont_impar, impar))
                cont_impar += 1
            impares = []
            cont_impar = 0

    for impar in impares:
        print('impar[%d] = %d' % (cont_impar, impar))
        cont_impar += 1
    for par in pares:
        print('par[%d] = %d' % (cont_par, par))
        cont_par += 1


main()