# coding: utf-8

nome1 = input()
nome2 = 'a'
nome3 = 'a'
animal = 'a'
if nome1 == 'vertebrado':
    nome2 = input()

    if nome2 == 'ave':
        nome3 = input()
        if nome3 == 'carnivoro':
            animal = 'aguia'
        elif nome3 == 'onivoro':
            animal = 'pomba'

    elif nome2 == 'mamifero':
        nome3 = input()
        if nome3 == 'onivoro':
            animal = 'homem'
        elif nome3 == 'herbivoro':
            animal = 'vaca'

elif nome1 == 'invertebrado':
    nome2 = input()
    if nome2 == 'inseto':
        nome3 = input()
        if nome3 == 'hematofago':
            animal = 'pulga'
        elif nome3 == 'herbivoro':
            animal = 'lagarta'

    elif nome2 == 'anelideo':
        nome3 = input()
        if nome3 == 'hematofago':
            animal = 'sanguessuga'
        elif nome3 == 'onivoro':
            animal = 'minhoca'

print(animal)