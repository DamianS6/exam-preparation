with open(r'dane/78/wiadomosci.txt') as dane:
    wiadomosci = [__.rstrip() for __ in dane.readlines()]

with open(r'dane/78/podpisy.txt') as dane:
    podpisy = [__.rstrip().split(' ') for __ in dane.readlines()]


def skrot(wiadomosc):
    s = [ord(__) for __ in 'ALGORYTM']
    numberofdots = 8 - (len(wiadomosc) % 8)
    wiadomosc += ''.join(['.' for __ in range(numberofdots)])
    n = 0
    for znak in wiadomosc:
        s[n] = (s[n] + ord(znak)) % 128
        n += 1
        if n == 8:
            n = 0
    wynik = ''
    for j in range(8):
        wynik += chr(65 + (s[j] % 26))
    return wynik


def deszyfr(podpis, d, n):
    wynik = ''
    for number in podpis:
        wynik += chr(int(number) * d % n)
    return wynik


"""
78.1.
Wyznacz skrót pierwszej wiadomości z pliku wiadomosci.txt i udokumentuj wyniki
kolejnych etapów obliczania tego skrótu. Zapisz w kolejnych wierszach pliku wynikowego:
a) liczbę znaków wiadomości po jej uzupełnieniu do najmniejszej długości
o wielokrotności 8 znaków,
b) wartości liczbowe 8 kolejnych bajtów skrótu (elementy tablicy S) po przetworzeniu
całej wiadomości — wszystkie wartości w jednym wierszu, oddzielone pojedynczymi
znakami odstępu,
c) skrót wiadomości w postaci napisu o długości 8, złożonego z wielkich liter alfabetu
angielskiego. """


def pierwsza(wiadomosc=wiadomosci[0]):
    with open(r'wyniki/78/epodpis_wynik.txt', 'w') as wyniki:
        wyniki.write('78.1\n')
        s = [ord(__) for __ in 'ALGORYTM']
        numberofdots = 8 - (len(wiadomosc) % 8)
        wiadomosc += ''.join(['.' for __ in range(numberofdots)])
        wyniki.write(f'{len(wiadomosc)}\n')
        n = 0
        for znak in wiadomosc:
            s[n] = (s[n] + ord(znak)) % 128
            n += 1
            if n == 8:
                n = 0
        for el in s:
            wyniki.write(f'{el} ')

        wynik = ''
        for j in range(8):
            wynik += chr(65 + (s[j] % 26))
        wyniki.write(f'\n{wynik}\n')


"""
78.2.
Odszyfruj skróty wiadomości ze wszystkich podpisów elektronicznych umieszczonych
w pliku podpisy.txt, stosując algorytm A z kluczem publicznym (d,n) = (3,200). Zapisz
uzyskane skróty w kolejnych, osobnych wierszach pliku z odpowiedziami. """


def skroty():
    with open(r'wyniki/78/epodpis_wynik.txt', 'a') as wyniki:
        wyniki.write('\n78.2\n')
        for wiadomosc in wiadomosci:
            wyniki.write(f'{skrot(wiadomosc)}\n')


"""
78.3.
Zweryfikuj wiarygodność wszystkich wiadomości i podaj numery wiadomości wiarygodnych.
Zapisz w jednym wierszu pliku z odpowiedziami, jako liczby z zakresu 1..11, zgodnie z kolejnością
umieszczenia ich w pliku danych, oddzielone pojedynczym znakiem odstępu. """


def wiarygodnosc():
    with open(r'wyniki/78/epodpis_wynik.txt', 'a') as wyniki:
        wyniki.write('\n78.3\n')
        for __ in range(1, 12):
            if deszyfr(podpisy[__-1], 3, 200) == skrot(wiadomosci[__-1]):
                wyniki.write(f'{__} ')

pierwsza()
skroty()
wiarygodnosc()