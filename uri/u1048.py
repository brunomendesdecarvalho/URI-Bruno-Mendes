# coding: utf-8

salario = float(input())
salario_final = 0
reajuste = 0

if (0 <= salario <= 400):
    reajuste = 0.15
    salario_final = salario + (salario * reajuste)
    print('Novo salario: %.2f' % salario_final)
    print('Reajuste ganho: %.2f' % (salario_final - salario))
    print('Em percentual:', int(reajuste * 100), '%')

elif (400 < salario <= 800):
    reajuste = 0.12
    salario_final = salario + (salario*reajuste)
    print('Novo salario: %.2f' %salario_final)
    print('Reajuste ganho: %.2f' %(salario_final-salario))
    print('Em percentual:', int(reajuste*100), '%')

elif (800 < salario <= 1200):
    reajuste = 0.1
    salario_final = salario + (salario * reajuste)
    print('Novo salario: %.2f' % salario_final)
    print('Reajuste ganho: %.2f' % (salario_final - salario))
    print('Em percentual:', int(reajuste * 100), '%')

elif (1200 < salario <= 2000):
    reajuste = 0.07
    salario_final = salario + (salario * reajuste)
    print('Novo salario: %.2f' % salario_final)
    print('Reajuste ganho: %.2f' % (salario_final - salario))
    print('Em percentual:', int(reajuste * 100), '%')

elif (salario > 2000):
    reajuste = 0.04
    salario_final = salario + (salario * reajuste)
    print('Novo salario: %.2f' % salario_final)
    print('Reajuste ganho: %.2f' % (salario_final - salario))
    print('Em percentual:', int(reajuste * 100), '%')