# coding: utf-8


def main():
    n = int(input())
    while n > 0:
        painel = input()
        quantidade = num_leds(painel)
        print('%d leds' % quantidade)
        n -= 1


def num_leds(painel):
    leds = 0
    for i in painel:
        if i == '1':
            leds += 2
        elif i == '2':
            leds += 5
        elif i == '3':
            leds += 5
        elif i == '4':
            leds += 4
        elif i == '5':
            leds += 5
        elif i == '6':
            leds += 6
        elif i == '7':
            leds += 3
        elif i == '8':
            leds += 7
        elif i == '9':
            leds += 6
        elif i == '0':
            leds += 6

    return leds


main()