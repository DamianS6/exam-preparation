with open(r'Arkusze/Maj_2015/Dane_PR/liczby.txt') as dane:
    liczby = [int(__.rstrip()) for __ in dane.readlines()]


def wiecej_zer():
    wiecej = 0
    for liczba in liczby:
        if str(liczba).count('0') > str(liczba).count('1'):
            wiecej += 1
    with open(r'Arkusze/Maj_2015/PESEL/wynik4.txt', 'w') as wyniki:
        wyniki.write(f'4.1.\n{wiecej}\n')


def podzielne():
    przez_dwa = 0
    przez_osiem = 0
    for liczba in liczby:
        if str(liczba).endswith('0'):
            przez_dwa += 1
        if str(liczba).endswith('000'):
            przez_osiem += 1
    with open(r'Arkusze/Maj_2015/PESEL/wynik4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.2.\nLiczby podzielne przez 2: {przez_dwa}\n'
                     f'Liczby podzielne przez 8: {przez_osiem}\n')


def minmax():
    najmniejsza_wiersz = 0
    najwieksza_wiersz = 0
    najmniejsza, najwieksza = liczby[0], liczby[0]
    for n in range(len(liczby)):
        if liczby[n] < najmniejsza:
            najmniejsza = liczby[n]
            najmniejsza_wiersz = n
        if liczby[n] > najwieksza:
            najwieksza = liczby[n]
            najwieksza_wiersz = n
    with open(r'Arkusze/Maj_2015/PESEL/wynik4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.3.\nWiersz najmniejszej liczby: {najmniejsza_wiersz}\n'
                     f'Wiersz najwiekszej liczby: {najwieksza_wiersz}\n')


wiecej_zer()
podzielne()
minmax()
