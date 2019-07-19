# coding: utf-8

alcool = 0
gasolina = 0
diesel = 0
n = 1

while n != 4:
    n = int(input())
    if n < 1 or n > 4:
        n = int(input())

    if n == 1:
        alcool += 1

    elif n == 2:
        gasolina += 1

    elif n == 3:
        diesel += 1

    elif n == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: %d' % alcool)
print('Gasolina: %d' % gasolina)
print('Diesel: %d' % diesel)