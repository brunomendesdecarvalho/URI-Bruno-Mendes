# coding: utf-8

# entradas
tempo_viagem = int(input())
velocidade_media = int(input())

# computação
qntde_litros = (tempo_viagem*velocidade_media)/12

# saída
print('%.3f' % qntde_litros)