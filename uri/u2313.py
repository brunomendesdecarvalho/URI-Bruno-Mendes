# coding: utf-8

lados = list(map(int, input().split(' ')))
lados = sorted(lados)

A, B, C = lados

if C >= A + B:
    print('Invalido')

elif C < A + B:

    if A == B and A == C:
        print('Valido-Equilatero')

    elif A == B and A != C or B == C and B != A:
        print('Valido-Isoceles')

    elif A != B and A != C and B != C:
        print('Valido-Escaleno')

    if (C**2) == (A**2) + (B**2):
        print('Retangulo: S')

    else:
        print('Retangulo: N')