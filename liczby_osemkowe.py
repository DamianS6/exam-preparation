with open(r'dane/62/liczby1.txt') as dane:
    liczby8 = [int(__.rstrip()) for __ in dane.readlines()]

with open(r'dane/62/liczby2.txt') as dane:
    liczby10 = [int(__.rstrip()) for __ in dane.readlines()]


"""
62.1
Wyszukaj w pliku liczby1.txt dwie liczby, najmniejszą i największą. Podaj wartości
tych liczb w zapisie ósemkowym."""


def minmax():
    najmniejsza, najwieksza = liczby8[0], liczby8[0]
    for n in liczby8:
        if n > najwieksza:
            najwieksza = n
        if n < najmniejsza:
            najmniejsza = n
    with open(r'wyniki/62/wyniki.txt', 'w') as wyniki:
        wyniki.write(f'62.1\nNajmniejsza: {najmniejsza}\nNajwieksza: {najwieksza}\n')


"""
62.2
Znajdź najdłuższy niemalejący ciąg liczb występujących w kolejnych wierszach pliku liczby2.
txt. Podaj pierwszy element tego ciągu oraz liczbę jego elementów. Możesz założyć,
że jest jeden taki ciąg. """


def niemalejacy():
    najdluzszy = 1
    elementy = 1
    for n in range(999):
        if liczby10[n] <= liczby10[n+1]:
            tymczasowy_pierwszy = liczby10[n]
            while liczby10[n] <= liczby10[n+1]:
                if n == 998:
                    break
                n += 1
                elementy += 1
            if elementy > najdluzszy:
                najdluzszy = elementy
                pierwszy = tymczasowy_pierwszy
            elementy = 1
    with open(r'wyniki/62/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'62.2\nNajdluzszy niemalejacy ciag w pliku liczby2.txt rozpoczyna sie liczba {pierwszy} '
                     f'i sklada sie z {najdluzszy} elementow.\n')


"""
62.3
Porównaj wartości liczb zapisanych w wierszach o tych samych numerach w plikach liczby1.
txt i liczby2.txt. Podaj liczbę wierszy, w których:
a) liczby mają w obu plikach taką samą wartość;
b) wartość liczby z pliku liczby1.txt jest większa od wartości liczby z pliku liczby2.txt. """


def porownanie():
    rowne, wieksze_w_liczby8 = 0, 0
    for n in range(1000):
        if int(str(liczby8[n]), 8) == liczby10[n]:
            rowne += 1
        if int(str(liczby8[n]), 8) > liczby10[n]:
            wieksze_w_liczby8 += 1
    with open(r'wyniki/62/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'62.3\na) {rowne} wierszy\nb) {wieksze_w_liczby8} wierszy\n')


"""
62.4
Podaj, ile razy w zapisie dziesiętnym wszystkich liczb z pliku liczby2.txt występuje
cyfra 6 oraz ile razy wystąpiłaby ta cyfra, gdyby te same liczby były zapisane w systemie
ósemkowym. """


def szostka():
    jest6, bylaby6 = 0, 0
    for n in range(1000):
        jest6 += str(liczby10[n]).count('6')
        bylaby6 += str(oct(liczby10[n])).count('6')
    with open(r'wyniki/62/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'62.4\nCyfra 6 w zapisie dziesietnym liczb z pliku liczby2.txt wystepuje {jest6} razy.\n'
                     f'Gdyby te samy liczby zapisac w systemie osemkowym, cyfra 6 wystapilaby {bylaby6} razy.\n')


minmax()
niemalejacy()
porownanie()
szostka()
