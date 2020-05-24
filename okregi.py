with open(r'dane/79/okregi.txt') as dane:
    okregi = []
    for __ in dane.readlines():
        okregi.append([float(item) for item in __.rstrip().split(' ') if item != ''])

i, ii, iii, iv = [], [], [], []

"""
79.1.
Podaj liczbę okręgów, które całkowicie zawierają się w I, II, III i IV ćwiartce układu współrzędnych.
Podaj również liczbę okręgów, które nie zawierają się w całości w żadnej ćwiartce,
tzn. mają co najmniej jeden punkt wspólny z jedną z osi Ox lub Oy. Jako odpowiedź wypisz
pięć liczb: liczba okręgów I ćwiartki, liczba okręgów II ćwiartki, liczba okręgów III ćwiartki,
liczba okręgów IV ćwiartki oraz liczba okręgów, które nie zawierają się w całości w żadnej
ćwiartce. """


def wcwiartce():
    I, II, III, IV, zadna = 0, 0, 0, 0, 0
    for okrag in okregi:
        if abs(okrag[2]) >= abs(okrag[0]) and abs(okrag[2]) >= abs(okrag[1]):
            zadna += 1
        elif okrag[0] > 0 and okrag[1] > 0:
            I += 1
            i.append(okrag)
        elif okrag[0] > 0 > okrag[1]:
            IV += 1
            iv.append(okrag)
        elif okrag[0] < 0 < okrag[1]:
            II += 1
            ii.append(okrag)
        else:
            III += 1
            iii.append(okrag)
    with open(r'wyniki/79/wyniki_okregi.txt', 'w') as wyniki:
        wyniki.write(f'79.1\nI cwiartka: {I}\nII cwiartka: {II}\n'
                     f'III cwiartka: {III}\nIV cwiartka: {IV}\nZadna: {zadna}\n')


"""
79.2.
Powiemy, że dwa okręgi tworzą lustrzaną parę, jeśli jeden z nich powstaje przez odbicie drugiego
względem jednej z osi Ox lub Oy. Podaj liczbę lustrzanych par spośród wszystkich
okręgów zapisanych w pliku okregi.txt. """


def lustrzane():
    liczba = 0
    for okrag in okregi:
        if okrag in i:
            for okrag2 in ii:
                if okrag[0] == -1 * okrag2[0] and okrag[2] == okrag2[2]:
                    liczba += 1
            for okrag4 in iv:
                if okrag[1] == -1 * okrag4[1] and okrag[2] == okrag4[2]:
                    liczba += 1
        elif okrag in iii:
            for okrag2 in ii:
                if okrag[1] == -1 * okrag2[1] and okrag[2] == okrag2[2]:
                    liczba += 1
            for okrag4 in iv:
                if okrag[0] == -1 * okrag4[0] and okrag[2] == okrag4[2]:
                    liczba += 1
    with open(r'wyniki/79/wyniki_okregi.txt', 'a') as wyniki:
        wyniki.write(f'\n79.2\n{liczba}\n')


"""79.3.
Powiemy, że dwa okręgi tworzą prostopadłą parę, jeśli jeden z nich powstaje przez obrót
drugiego o 90 stopni względem środka układu współrzędnych.
Przykład: okręgi o środkach w punktach (3,-5), (5,3) (i o tych samych promieniach) tworzą
parę prostopadłą; zob. rysunek.
Podaj liczbę prostopadłych par okręgów spośród wszystkich okręgów zapisanych w pliku
okregi.txt. """


def prostopadle():
    liczba = 0
    for okrag in okregi:
        if okrag in i:
            for okrag2 in ii:
                if okrag[0] == okrag2[1] and okrag[1] == -1 * okrag2[0] and okrag[2] == okrag2[2]:
                    liczba += 1
            for okrag4 in iv:
                if okrag[1] == okrag4[0] and okrag[0] == -1 * okrag4[1] and okrag[2] == okrag4[2]:
                    liczba += 1
        elif okrag in iii:
            for okrag2 in ii:
                if okrag[0] == -1 * okrag2[1] and okrag[1] == okrag2[0] and okrag[2] == okrag2[2]:
                    liczba += 1
            for okrag4 in iv:
                if okrag[0] == okrag4[1] and okrag[1] == -1 * okrag4[0] and okrag[2] == okrag4[2]:
                    liczba += 1
    with open(r'wyniki/79/wyniki_okregi.txt', 'a') as wyniki:
        wyniki.write(f'\n79.3\n{liczba}\n\n79.4\n')


"""
79.4.
Powiemy, że ciąg okręgów tworzy łańcuch, jeśli kolejne okręgi tego ciągu mają ze sobą co
najmniej jeden punkt wspólny; przyjmujemy, że ciąg zawierający tylko jeden okrąg również
tworzy łańcuch.
Znajdź długości wszystkich łańcuchów tworzonych przez okręgi zapisane w wierszach
o numerach od 1 do 1000. Podaj długość najdłuższego łańcucha. """


def lancuchy():
    dlugosc = 1
    najdluzszy = 1
    n = 0
    while n < 1000:
        dist = abs(((okregi[n][0] - okregi[n+1][0])**2 + (okregi[n][1] - okregi[n+1][1])**2))**(1/2)
        if dist > okregi[n][2] + okregi[n+1][2] or dist < abs(okregi[n][2] - okregi[n+1][2]):
            if dlugosc > najdluzszy:
                najdluzszy = dlugosc
            with open(r'wyniki/79/wyniki_okregi.txt', 'a') as wyniki:
                wyniki.write(f'{dlugosc} ')
            dlugosc = 1
        else:
            dlugosc += 1
        n += 1
    with open(r'wyniki/79/wyniki_okregi.txt', 'a') as wyniki:
        wyniki.write(f'\n{najdluzszy}')


wcwiartce()
lustrzane()
prostopadle()
lancuchy()