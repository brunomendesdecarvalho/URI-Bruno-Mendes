# coding: utf-8

# entrada de dados
nome_funcionario = input()
salario_funcionario = float(input())
bonus_vendas = float(input())

# computações

salario_total = salario_funcionario + (0.15*bonus_vendas)

# saída
print('TOTAL = R$ %.2f' % salario_total)