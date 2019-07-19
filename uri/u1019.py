# coding: utf-8

# entradas
tempo_total = int(input())

# computações
quantidade_horas = str(tempo_total//3600)
quantidade_minutos = str((tempo_total%3600)//60)
quantidade_segundos = str((tempo_total%3600)%60)

# saídas
print(quantidade_horas + ':' + quantidade_minutos +
      ':' + quantidade_segundos)