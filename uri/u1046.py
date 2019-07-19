# coding: utf-8

hora_inicial, hora_final = input().split(" ")
hora_inicial, hora_final = int(hora_inicial), int(hora_final)
horas = 0
if hora_inicial == hora_final:
    horas = 24
else:
    horas = hora_final - hora_inicial
    if horas < 0:
        horas += 24

print('O JOGO DUROU %d HORA(S)' %(horas))