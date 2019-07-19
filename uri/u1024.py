# coding: utf-8
from math import ceil
n = int(input())
i = 0
digitos = 0
while(i < n):
    i += 1
    string = input()
    digitos = len(string)
    aux1 = string
    string = []

    while digitos > 0:
        aux2 = aux1[digitos-1]
        if 65 <= ord(aux2) <= 90 or 97 <= ord(aux2) <= 122:
            aux2 = chr(ord(aux2)+3)
        if digitos <= ceil(len(aux1)/2):
            aux2 = chr(ord(aux2)-1)
        string.append(aux2)
        digitos -= 1

    string = ''.join(map(str, string))
    print(string)