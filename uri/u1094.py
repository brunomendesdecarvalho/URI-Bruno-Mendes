# coding: utf-8

N = int(input())
Quantia = 0
Tipo = 'null'
capachos = {}
total = 0
porcento = '%'
while N > 0:
    Quantia, Tipo = input().split(' ')
    Quantia = int(Quantia)
    total += Quantia
    if Tipo.isupper() == False:
        Tipo.switchcase()

    if Tipo not in capachos.keys():
        capachos[Tipo] = Quantia

    elif Tipo in capachos.keys():
        capachos[Tipo] += Quantia
    N -= 1

print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % capachos['C'])
print('Total de ratos: %d' % capachos['R'])
print('Total de sapos: %d' % capachos['S'])
print('Percentual de coelhos: %.2f %s' % (100*(capachos['C']/total), porcento))
print('Percentual de ratos: %.2f %s' % (100*(capachos['R']/total), porcento))
print('Percentual de sapos: %.2f %s' % (100*(capachos['S']/total), porcento))

