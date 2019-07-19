#coding: utf-8

p1, n1, v1 = input().split(" ")
p1 = int(p1)
n1 = int(n1)
v1 = float(v1)

p2, n2, v2 = input().split(" ")
p2 = int(p2)
n2 = int(n2)
v2 = float(v2)

print('VALOR A PAGAR: R$ %.2f' %(n1*v1 + n2*v2))