import time
start = time.time()


with open(r'dane/64/dane_obrazki.txt') as dane:
    obrazki = [[] for __ in range(200)]
    l = 0
    for __ in dane.readlines():
        if len(__) < 20:
            continue
        obrazki[l].append(__.rstrip())
        if len(obrazki[l]) == 21:
            l += 1


"""
64.1
Obrazek nazywamy rewersem, jeśli liczba występujących w nim pikseli czarnych jest większa
od liczby pikseli białych. Podaj, ile jest w pliku obrazków, które są rewersami.
Podaj też największą liczbę pikseli czarnych występujących w jednym obrazku. """


def rewers():
    rewersy = 0
    najwiecej = 0
    for obrazek in obrazki:
        czarne = 0
        for linia in obrazek[:20]:
            czarne += list(linia[:20]).count('1')
        if czarne > 200:
            if czarne > najwiecej:
                najwiecej = czarne
            rewersy += 1
    with open(r'wyniki/64/wyniki_obrazki.txt', 'w') as wyniki:
        wyniki.write(f'64.1\n{rewersy} rewersow. Najwieksza liczba czarnych pikseli w jednym obrazku: {najwiecej}.\n')


"""
64.2
Obrazek rozmiaru n × n będziemy nazywać rekurencyjnym, jeśli n jest parzyste oraz obrazek
składa się z 4 kopii tego samego obrazka rozmiaru n/2 x n/2. 
Podaj liczbę obrazków rekurencyjnych w pliku wejściowym. Ponadto podaj opis pierwszego
obrazka rekurencyjnego występującego w pliku. """


def rekurencyjny():
    rekurencyjne = 0
    for obrazek in obrazki:
        rekurencja = True
        for wiersz in range(10):
            if obrazek[wiersz][:10] == obrazek[wiersz][10:20] == \
                    obrazek[wiersz + 10][:10] == obrazek[wiersz + 10][10:20]:
                pass
            else:
                rekurencja = False
                break
        if rekurencja:
            if rekurencyjne == 0:
                pierwszy = obrazek
            rekurencyjne += 1

    with open(r'wyniki/64/wyniki_obrazki.txt', 'a') as wyniki:
        wyniki.write(f'64.2\nLiczba rekurencyjnych obrazkow: {rekurencyjne}.\nPierwszy rekurencyjny obrazek:\n')
        for linia in pierwszy[:20]:
            wyniki.write(linia[:20] + '\n')


"""
64.3
Obrazek nazywamy poprawnym, jeśli wszystkie bity parzystości są w nim poprawne (zarówno
w wierszach, jak i kolumnach). Obrazek nazywamy naprawialnym, jeśli nie jest poprawny,
a jednocześnie co najwyżej jeden bit parzystości wiersza i co najwyżej jeden bit parzystości
kolumny jest w nim niepoprawny.
Natomiast nienaprawialnym nazywamy obrazek, który nie jest poprawny i nie jest naprawialny.
Podaj liczbę obrazków poprawnych, liczbę obrazków naprawialnych oraz liczbę obrazków
nienaprawialnych. Ponadto podaj największą liczbę błędnych bitów parzystości występujących
w jednym obrazku. """


def poprawnosc():
    poprawne, naprawialne, nienaprawialne, najwiecej = 0, 0, 0, 0
    for obrazek in obrazki:
        bledy_wiersza, bledy_kolumny = 0, 0
        for wiersz in range(20):  # Zliczanie błędów w wierszach
            if list(obrazek[wiersz][:20]).count("1") % 2 != int(obrazek[wiersz][20]):
                bledy_wiersza += 1

        for kolumna in range(20):  # Zliczanie błędów w kolumnach
            jedynki = 0
            for wiersz in obrazek[:20]:
                if wiersz[kolumna] == '1':
                    jedynki += 1
            if jedynki % 2 != int(obrazek[20][kolumna]):
                bledy_kolumny += 1

        if bledy_kolumny == 0 and bledy_wiersza == 0:
            poprawne += 1
        elif bledy_wiersza + bledy_kolumny == 1 or (bledy_wiersza == 1 and bledy_kolumny == 1):
            naprawialne += 1
        else:
            nienaprawialne += 1
            if bledy_kolumny + bledy_wiersza > najwiecej:
                najwiecej = bledy_wiersza + bledy_kolumny

    with open(r'wyniki/64/wyniki_obrazki.txt', 'a') as wyniki:
        wyniki.write(f'64.3\nPoprawne: {poprawne}, naprawialne: {naprawialne}, nienaprawialne: {nienaprawialne}, '
                     f'najwieksza liczba bledow w jednym obrazku: {najwiecej}.\n')


"""
64.4
W obrazku naprawialnym wystarczy zmienić jedną wartość, aby uzyskać obrazek poprawny.
Dokładniej, jeśli niepoprawne są bity parzystości i-tego wiersza i j-tej kolumny, wystarczy
zmienić j-ty piksel w i-tym wierszu. Jeśli niepoprawny jest dokładnie jeden bit parzystości
(wiersza albo kolumny), wystarczy zmienić ten bit parzystości.
Podaj numery obrazków naprawialnych, przyjmując, że numery kolejnych obrazków w pliku
to 1, 2, 3 itd. Przy numerze każdego obrazka naprawialnego podaj numer wiersza i kolumny
wartości, którą wystarczy zmienić, aby uzyskać obrazek poprawny. """


def naprawianie():  # Jest to osobna funkcja mimo zbieżności z poprzednią aby zachować kolejność odpowiedzi.
    with open(r'wyniki/64/wyniki_obrazki.txt', 'a') as wyniki:
        wyniki.write(f'64.4\n')
    numer_obrazka = 1
    for obrazek in obrazki:
        numer_wiersza, numer_kolumny = 1, 1
        bledy_wiersza, bledy_kolumny = 0, 0
        for wiersz in range(20):  # Zliczanie błędów w wierszach
            if list(obrazek[wiersz][:20]).count("1") % 2 != int(obrazek[wiersz][20]):
                numer_wiersza = wiersz+1
                bledy_wiersza += 1

        for kolumna in range(20):  # Zliczanie błędów w kolumnach
            jedynki = 0
            for wiersz in obrazek[:20]:
                if wiersz[kolumna] == '1':
                    jedynki += 1
            if jedynki % 2 != int(obrazek[20][kolumna]):
                numer_kolumny = kolumna+1
                bledy_kolumny += 1

        if bledy_wiersza == 1 and bledy_kolumny == 0:
            with open(r'wyniki/64/wyniki_obrazki.txt', 'a') as wyniki:
                wyniki.write(f'Obrazek {numer_obrazka}, wiersz {numer_wiersza}, kolumna 21.\n')
        elif bledy_wiersza == 0 and bledy_kolumny == 1:
            with open(r'wyniki/64/wyniki_obrazki.txt', 'a') as wyniki:
                wyniki.write(f'Obrazek {numer_obrazka}, wiersz 21, kolumna {numer_kolumny}.\n')
        elif bledy_wiersza == 1 and bledy_kolumny == 1:
            with open(r'wyniki/64/wyniki_obrazki.txt', 'a') as wyniki:
                wyniki.write(f'Obrazek {numer_obrazka}, wiersz {numer_wiersza}, kolumna {numer_kolumny}.\n')

        numer_obrazka += 1


rewers()
rekurencyjny()
poprawnosc()
naprawianie()
print("--- %s seconds ---" % (time.time() - start))
