contador = 0
N = int(input())
ho = ''

while contador <= N:
    contador += 1
    if contador < N:
        ho += 'Ho '
    elif contador == N:
        ho += 'Ho!'

print(ho)