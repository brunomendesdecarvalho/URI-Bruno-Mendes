# coding: utf-8


def main():
    while True:
        try:
            a, b = map(int, input().split(' '))
            print(a^b)
        
        except EOFError:
            break
    
    
main()