# coding: utf-8


def main():
    vetor = []
    while len(vetor) < 10:
        vetor.append(int(input()))
    for i in range(0, len(vetor)):
        if vetor[i] <= 0:
            vetor[i] = 1
        else:
            pass

        print('X[%d] = %d' % (i, vetor[i]))


main()