# coding: utf-8


def main():
    while True:
        try:
            string = input()
            dancing_sentence(string)

        except EOFError:
            break


def dancing_sentence(string):
    upper = True
    nova_string = ''

    for i in string:
        if is_letter(i) == False:
            nova_string += i
            continue

        elif is_letter(i) == True:

            if upper == True:
                nova_string += i.upper()
                upper = False

            elif upper == False:
                nova_string += i.lower()
                upper = True

    print(nova_string)


def is_letter(string):
    if 65 <= ord(string) <= 90 or 97 <= ord(string) <= 122:
        return True
    else:
        return False


main()