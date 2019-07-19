# coding: utf-8


def main():
    n = int(input())
    while n > 0:
        string = input()
        descriptografar(string)
        n -= 1

def descriptografar(string):
    nova_string = ''
    for i in string:
        if 97 <= ord(i) <= 122:
            nova_string += i
        else:
            pass
    nova_string = nova_string[::-1]
    print(nova_string)


main()