# coding: utf-8

grenal = 1
quantidade = 0
vit_inter = 0
vit_gremio = 0
empates = 0

while grenal == 1:
    inter, gremio = map(int, input().split())
    quantidade += 1

    if inter > gremio:
        vit_inter += 1

    elif inter < gremio:
        vit_gremio += 1

    elif inter == gremio:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')
    grenal = int(input())

print('%d grenais' % quantidade)
print('Inter:%d' % vit_inter)
print('Gremio:%d' % vit_gremio)
print('Empates:%d' % empates)

if vit_inter > vit_gremio:
    print('Inter venceu mais')

elif vit_inter < vit_gremio:
    print('Gremio venceu mais')

elif vit_inter == vit_gremio:
    print('Nao houve vencedor')