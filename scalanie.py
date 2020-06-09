with open(r'Arkusze/Czerwiec_2018/dane1.txt') as dane:
    dane1 = [__.rstrip().split() for __ in dane.readlines()]

with open(r'Arkusze/Czerwiec_2018/dane2.txt') as dane:
    dane2 = [__.rstrip().split() for __ in dane.readlines()]


# 4.1.
def porownanie():
    ile = 0
    for n in range(len(dane1)):
        if dane1[n][-1] == dane2[n][-1]:
            ile += 1
    with open(r'Arkusze/Czerwiec_2018/wynik4_1.txt', 'w') as wynik:
        wynik.write(str(ile))


# 4.2.
def parzyste():
    ile = 0
    for n in range(len(dane1)):
        parzyste1, nieparzyste1 = 0, 0
        parzyste2, nieparzyste2 = 0, 0
        for wyraz in dane1[n]:
            if int(wyraz) % 2 == 0:
                parzyste1 += 1
            else:
                nieparzyste1 += 1
        for wyraz in dane2[n]:
            if int(wyraz) % 2 == 0:
                parzyste2 += 1
            else:
                nieparzyste2 += 1
        if parzyste1 == 5 and parzyste2 == 5 and nieparzyste1 == 5 and nieparzyste2 == 5:
            ile += 1
    with open(r'Arkusze/Czerwiec_2018/wynik4_2.txt', 'w') as wynik:
        wynik.write(str(ile))


# 4.3.
def takie_same():
    ile = 0
    numery = []
    for n in range(len(dane1)):
        wyrazy1, wyrazy2 = [], []
        for wyraz in dane1[n]:
            if wyraz not in wyrazy1:
                wyrazy1.append(wyraz)
        for wyraz in dane2[n]:
            if wyraz not in wyrazy2:
                wyrazy2.append(wyraz)
        if sorted(wyrazy1) == sorted(wyrazy2):
            ile += 1
            numery.append(n+1)
    with open(r'Arkusze/Czerwiec_2018/wynik4_3.txt', 'w') as wynik:
        wynik.write(f'{str(ile)} para ciagow\nnumery wierszy: {numery[0]}')


# 4.4.
def sortowanie():
    with open(r'Arkusze/Czerwiec_2018/wynik4_4.txt', 'w') as wynik:
        for n in range(len(dane1)):
            scalony = []
            w1, w2 = 0, 0
            for l in range(20):
                if w1 == 10:
                    scalony.append(int(dane2[n][w2]))
                    w2 += 1
                elif w2 == 10:
                    scalony.append(int(dane1[n][w1]))
                    w1 += 1
                elif int(dane1[n][w1]) <= int(dane2[n][w2]):
                    scalony.append(int(dane1[n][w1]))
                    w1 += 1
                else:
                    scalony.append(int(dane2[n][w2]))
                    w2 += 1
            for x in scalony:
                wynik.write(f'{x} ')
            wynik.write(f'\n')


porownanie()
parzyste()
takie_same()
sortowanie()
