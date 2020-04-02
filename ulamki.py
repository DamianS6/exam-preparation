import time
import math
start = time.time()


with open(r'dane/65/dane_ulamki.txt') as dane:
    ulamki = [list(__.rstrip().split(' ')) for __ in dane.readlines()]

for ulam in ulamki:
    ulam[0], ulam[1] = int(ulam[0]), int(ulam[1])


"""
65.1.
Podaj ułamek o minimalnej wartości. Jeśli w pliku występuje więcej niż jeden taki ułamek, to
podaj ten spośród nich, który ma najmniejszy mianownik. Twoja odpowiedź powinna zawierać
parę liczb oznaczającą licznik i mianownik ułamka. """


def minimalna():
    minim = [12000, 1]
    for ul in ulamki:
        licznik = ul[0]
        mianownik = ul[1]
        if licznik / mianownik < minim[0] / minim[1]:
            minim = [licznik, mianownik]
        if licznik / mianownik == minim[0] / minim[1] and mianownik < minim[1]:
            minim = [licznik, mianownik]
    with open(r'wyniki/65/wyniki_ulamki.txt', 'w') as wyniki:
        wyniki.write(f'65.1.\n{minim[0]} {minim[1]}\n')


"""
65.2.
Podaj liczbę zapisanych w pliku ułamków, które zostały podane w postaci nieskracalnej. """


def nieskracalne(ul):
    nieskracalny = False
    if math.gcd(ul[0], ul[1]) == 1:
        nieskracalny = True
    return nieskracalny


def licz_nieskracalne():
    liczba = 0
    for ulamek in ulamki:
        if nieskracalne(ulamek):
            liczba += 1
    with open(r'wyniki/65/wyniki_ulamki.txt', 'a') as wyniki:
        wyniki.write(f'65.2.\n{liczba}\n')


"""
65.3.
Zapis danych w postaci nieskracalnej uzyskamy, zamieniając każdy ułamek na jego postać
nieskracalną. Podaj sumę liczników wszystkich podanych w pliku ułamków, jaką otrzymalibyśmy
po sprowadzeniu ułamków do nieskracalnej postaci. """


def suma_licznikow():
    suma = 0
    for ul in ulamki:
        s = ul[0]
        if not nieskracalne(ul):
            s = ul[0] / math.gcd(ul[0], ul[1])
        suma += int(s)
    with open(r'wyniki/65/wyniki_ulamki.txt', 'a') as wyniki:
        wyniki.write(f'65.3.\n{suma}\n')


"""
65.4.
Ułamki w pliku zostały tak dobrane, że każdy mianownik jest dzielnikiem liczby
b = 2**2 * 3**2 * 5**2 * 7**2 * 13, a wartość każdego ułamka jest nie większa niż 3.
Oznacza to, że sumę wszystkich ułamków można przedstawić jako ułamek a/b,
którego mianownikiem jest b = 2**2 * 3**2 * 5**2 * 7**2 * 13. Wyznacz sumę ułamków
ze wszystkich wierszy i podaj licznik takiego ułamka, że suma ułamków jest równa a/b. """


def mianownik_b():
    licznik = 0
    b = 2*3*5*7*13
    b = b*b/13
    for ul in ulamki:
        licznik += int((ul[0] * b) / ul[1])
    with open(r'wyniki/65/wyniki_ulamki.txt', 'a') as wyniki:
        wyniki.write(f'65.4.\n{licznik}\n')


minimalna()
licz_nieskracalne()
suma_licznikow()
mianownik_b()

print('--- %s seconds ---' % (time.time() - start))
