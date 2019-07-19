# coding: utf-8

salario = float(input())
imposto = 0
isento = 0

if salario <= 2000:
    print('Isento')
else:
    salario -= 2000
    if 0 < salario <= 1000:
        imposto += salario * 0.08
    else:
        salario -= 1000
        if 0 < salario <= 1500:
            imposto += 1000*0.08 + salario*0.18
        else:
            salario -= 1500
            imposto += 1000*0.08 + 1500*0.18 + salario*0.28

    print('R$ %.2f' % imposto)