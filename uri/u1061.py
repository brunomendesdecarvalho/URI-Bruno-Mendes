# coding: utf-8

# entradas:


dia_inicio = input().split(' ')
dia_inicio = int(dia_inicio[1])
horas_inicio, minutos_inicio, segundos_inicio = map(int, input().split(' : '))

dia_fim = input().split(' ')
dia_fim = int(dia_fim[1])
horas_fim, minutos_fim, segundos_fim = map(int, input().split(' : '))

# computações:

duracao_dias = dia_fim - dia_inicio

duracao_horas = horas_fim - horas_inicio
if duracao_horas < 0:
    duracao_dias -= 1
    duracao_horas += 24

duracao_minutos = minutos_fim - minutos_inicio
if duracao_minutos < 0:
    duracao_horas -= 1
    duracao_minutos += 60

duracao_segundos = segundos_fim - segundos_inicio
if duracao_segundos < 0:
    duracao_minutos -= 1
    duracao_segundos += 60

if duracao_dias <= 0:
    duracao_dias = 0

# saídas:

print('%d dia(s)' % duracao_dias)
print('%d hora(s)' % duracao_horas)
print('%d minuto(s)'% duracao_minutos)
print('%d segundo(s)' % duracao_segundos)
