# coding: utf-8

# entrada:

a, b = input().split(" ")
a, b = int(a), int(b)

if(b%a and a%b != 0):
    print('Nao sao Multiplos')

elif(b%a == 0 or a%b == 0):
    print('Sao Multiplos')