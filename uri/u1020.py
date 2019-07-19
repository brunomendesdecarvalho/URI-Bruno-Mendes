# coding: utf-8

# entradas
idade = int(input())

# computações
quantidade_anos = idade//365
quantidade_meses = (idade%365)//30
quantidade_dias = (idade%365)%30

# saídas
print('%.f ano(s)' % quantidade_anos)
print('%.f mes(es)' % quantidade_meses)
print('%.f dia(s)' % quantidade_dias)