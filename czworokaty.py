with open(r'dane/81/wspolrzedne.txt') as dane:
    wspolrzedne = []
    wspolrzedne_tekst = [__.rstrip().split('\t') for __ in dane.readlines()]
    for __ in wspolrzedne_tekst:
        wspolrzedne.append([int(wartosc) for wartosc in __])

with open(r'dane/81/wspolrzedneTR.txt') as dane:
    wierzcholki = []
    wierzcholki_tekst = [__.rstrip().split('\t') for __ in dane.readlines()]
    for __ in wierzcholki_tekst:
        wierzcholki.append([int(wartosc) for wartosc in __])

"""
81.1.
Podaj liczbę wierszy z pliku wierzcholki.txt, w których wszystkie zapisane punkty
leżą w I ćwiartce układu współrzędnych i nie należą do osi OX i OY. """


def pierwsza():
    liczba_wierszy = 0
    for __ in wspolrzedne:
        wszystkie = True
        for wspolrzedna in __:
            if wspolrzedna <= 0:
                wszystkie = False
                break
        if wszystkie:
            liczba_wierszy += 1
    with open(r'wyniki/81/wyniki.txt', 'w') as wyniki:
        wyniki.write(f'81.1\n{liczba_wierszy}\n')


"""
81.2.
Podaj liczbę wierszy z pliku wierzcholki.txt, w których zapisane są współrzędne punktów
leżących na jednej prostej. """


def prosta():
    jedna_prosta = 0
    for __ in wspolrzedne:
        if __[2] - __[0] == 0:
            x = __[0]
            if __[4] == x:
                jedna_prosta += 1
        elif __[3] - __[1] == 0:
            y = __[1]
            if __[5] == y:
                jedna_prosta += 1
        else:
            a = (__[3] - __[1]) / (__[2] - __[0])
            b = __[1] - __[0]*a
            if __[5] == a*__[4] + b:
                jedna_prosta += 1
    with open(r'wyniki/81/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n81.2\n{jedna_prosta}\n\n81.3\n')


"""
81.3.
Podaj (z pliku wierzcholkiTR.txt) współrzędne wierzchołków trójkąta o największym
obwodzie oraz obwód tego trójkąta. Obwód zaokrąglij do dwóch miejsc po przecinku. Uwaga:
możesz założyć, że jest tylko jeden taki trójkąt. 

81.4.
Dla każdego wiersza z pliku wierzcholkiTR.txt sprawdź, czy punkty zapisane w tym
wierszu są wierzchołkami pewnego trójkąta prostokątnego. Podaj liczbę trójkątów prostokątnych
zapisanych w tym pliku. """


def obwod_prostokatne():
    najwiekszy = 1
    liczba_prostokatnych = 0
    for __ in wierzcholki:
        dlugosc1 = ((__[0] - __[2])**2 + (__[1] - __[3])**2)**(1/2)
        dlugosc2 = ((__[0] - __[4])**2 + (__[1] - __[5])**2)**(1/2)
        dlugosc3 = ((__[2] - __[4])**2 + (__[3] - __[5])**2)**(1/2)
        if dlugosc1 + dlugosc2 + dlugosc3 > najwiekszy:
            najwiekszy = dlugosc1 + dlugosc2 + dlugosc3
            naj_wierzcholki = [wierzch for wierzch in __]
        if dlugosc1**2 == dlugosc2**2 + dlugosc3**2 or dlugosc2**2 == dlugosc1**2 + dlugosc3**2 \
                or dlugosc3 ** 2 == dlugosc2 ** 2 + dlugosc1 ** 2:
            liczba_prostokatnych += 1
    with open(r'wyniki/81/wyniki.txt', 'a') as wyniki:
        for __ in naj_wierzcholki:
            wyniki.write(f"{str(__)} ")
        wyniki.write(f"\nObwod: {round(najwiekszy, 2)}\n\n81.4\n{liczba_prostokatnych}\n")


pierwsza()
prosta()
obwod_prostokatne()