#coding: utf-8

din = int(input())

r100 = din//100
r50 = (din%100)//50
r20 = ((din%100)%50)//20
r10 = (((din%100)%50)%20)//10
r5 = ((((din%100)%50)%20)%10)//5
r2 = (((((din%100)%50)%20)%10)%5)//2
r1 = (((((din%100)%50)%20)%10)%5)%2


print(din)
print(r100, 'nota(s) de R$ 100,00')
print(r50, 'nota(s) de R$ 50,00')
print(r20, 'nota(s) de R$ 20,00')
print(r10, 'nota(s) de R$ 10,00')
print(r5, 'nota(s) de R$ 5,00')
print(r2, 'nota(s) de R$ 2,00')
print(r1, 'nota(s) de R$ 1,00')