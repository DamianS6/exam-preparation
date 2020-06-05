with open(r'Arkusze/Czerwiec_2016/liczby.txt') as dane:
    liczby = [__.rstrip() for __ in dane.readlines()]


# 6.1.
def osemkowy():
    ile = 0
    for liczba in liczby:
        if liczba[-1] == '8':
            ile += 1
    with open(r'Arkusze/Czerwiec_2016/wyniki_6_1.txt', 'w') as wyniki:
        wyniki.write(f'6.1.\n{ile}\n')


# 6.2.
def czworkowy_bez_0():
    ile = 0
    for liczba in liczby:
        if liczba[-1] == '4' and '0' not in liczba:
            ile += 1
    with open(r'Arkusze/Czerwiec_2016/wyniki_6_2.txt', 'w') as wyniki:
        wyniki.write(f'6.2.\n{ile}\n')


# 6.3.
def dwojkowe_parzyste():
    ile = 0
    for liczba in liczby:
        if liczba[-1] == '2' and liczba[-2] == '0':
            ile += 1
    with open(r'Arkusze/Czerwiec_2016/wyniki_6_3.txt', 'w') as wyniki:
        wyniki.write(f'6.3.\n{ile}\n')


# 6.4.
def suma_osemkowych():
    suma = 0
    for liczba in liczby:
        if liczba[-1] == '8':
            suma += int(liczba[:-1], 8)
    with open(r'Arkusze/Czerwiec_2016/wyniki_6_4.txt', 'w') as wyniki:
        wyniki.write(f'6.4.\n{suma}\n')


# 6.5.
def minmax():
    najmn, najw = int(liczby[0][:-1], int(liczby[0][-1])), int(liczby[0][:-1], int(liczby[0][-1]))
    kod_najmn, kod_najw = liczby[0], liczby[0]
    for liczba in liczby:
        if int(liczba[:-1], int(liczba[-1])) > najw:
            najw = int(liczba[:-1], int(liczba[-1]))
            kod_najw = liczba
        if int(liczba[:-1], int(liczba[-1])) < najmn:
            najmn = int(liczba[:-1], int(liczba[-1]))
            kod_najmn = liczba
    with open(r'Arkusze/Czerwiec_2016/wyniki_6_5.txt', 'w') as wyniki:
        wyniki.write(f'6.5.\nKody: {kod_najw} {kod_najmn}\nWartosci: {najw} {najmn}')


osemkowy()
czworkowy_bez_0()
dwojkowe_parzyste()
suma_osemkowych()
minmax()
