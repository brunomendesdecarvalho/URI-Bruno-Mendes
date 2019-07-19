#coding: utf-8

def unfair(EV1, EV2, AT): # Gambler's Ruin

    if (AT==3.0):
        prob = EV1/(EV1+EV2)

    else:
        p = 1.0 - ((6-AT)/6.0)
        p = (1.0-p)/p
        prob = (1.0 - (p**EV1))/(1.0 - (p**(EV1 + EV2)))

    return prob

EV1, EV2, AT, D = 1, 1, 1, 1

while (EV1 != 0 and EV2 != 0 and AT != 0 and D != 0 ):

    EV1, EV2, AT, D = input().split(" ")
    EV1, EV2, AT, D = int(EV1), int(EV2), int(AT), int(D)

    if (EV1 == 0 and EV2 == 0 and AT == 0 and D == 0):
        break
    else:
        aux = EV1 # aux - variável auxiliar para simular vitória dos vampiros
        EV1 = 0

        while aux > 0:
            aux -= D
            EV1 += 1

        aux = EV2
        EV2 = 0

        while aux > 0:
            aux -= D
            EV2 += 1

        prob = unfair(EV1, EV2, AT)
        print('%.1f' %(prob*100))