# coding: utf-8

# entradas:

entrada = [int(i) for i in input().split(" ")]
hora_inicial = entrada[0]
minuto_inicial = entrada[1]
hora_final = entrada[2]
minuto_final = entrada[3]

# computações:

horas = hora_final - hora_inicial

if horas < 0:
    horas += 24

minutos = minuto_final - minuto_inicial

if minutos < 0:
    minutos += 60
    horas -= 1

# saídas:

if horas == 0 and minutos == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(horas, minutos))
