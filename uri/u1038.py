# coding: utf-8

# entradas

codigo, quantidade = input().split(" ")
valor = 0
# computações e saídas

codigo, quantidade = int(codigo), int(quantidade)

if (codigo == 1):
    valor = 4.0*quantidade
    print('Total: R$ %.2f' % valor)

elif(codigo == 2):
    valor = 4.5*quantidade
    print('Total: R$ %.2f' % valor)

elif(codigo == 3):
    valor = 5.0*quantidade
    print('Total: R$ %.2f' % valor)

elif(codigo == 4):
    valor = 2.0*quantidade
    print('Total: R$ %.2f' % valor)

elif(codigo == 5):
    valor = 1.5*quantidade
    print('Total: R$ %.2f' % valor)