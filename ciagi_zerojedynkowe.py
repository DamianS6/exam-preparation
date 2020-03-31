import time
start = time.time()

with open(r'dane/63/ciagi.txt') as dane:
    ciagi = [int(__.rstrip()) for __ in dane.readlines()]


"""
63.1
Ciągiem dwucyklicznym będziemy nazywać taki ciąg zerojedynkowy 􀝓 o długości parzystej,
który składa się z dwóch fragmentów w1 oraz w2, w = w1w2, takich że w1 = w2. Podaj
wszystkie ciągi dwucykliczne zapisane w pliku ciagi.txt. """


def dwucykliczne():
    with open(r'wyniki/63/wyniki_ciagi.txt', 'w') as wyniki:
        wyniki.write('61.1\n')
    for ciag in ciagi:
        ciag = list(str(ciag))
        dlugosc = len(ciag)
        if dlugosc % 2 != 0:
            continue
        if ciag[:dlugosc//2] == ciag[dlugosc//2:]:
            with open(r'wyniki/63/wyniki_ciagi.txt', 'a') as wyniki:
                wyniki.write(''.join(ciag) + '\n')


"""
63.2
Podaj liczbę ciągów z pliku ciagi.txt, w których nie występują obok siebie dwie jedynki. """


def sasiadki():
    ile = 0
    for ciag in ciagi:
        if '11' not in str(ciag):
            ile += 1
    with open(r'wyniki/63/wyniki_ciagi.txt', 'a') as wyniki:
        wyniki.write(f'\n62.2\n{ile}\n')


"""
63.3
Liczbą półpierwszą nazywamy taką liczbę, która jest iloczynem dwóch liczb pierwszych.
Podaj, ile ciągów z pliku ciagi.txt jest reprezentacją binarną liczb półpierwszych. Dodatkowo
podaj największą i najmniejszą liczbę półpierwszą w zapisie dziesiętnym."""


def polpierwsze():
    pierwsze = [2]
    for n in range(2, 2**18//2+2):  # Przygotowanie listy liczb pierwszych.
        pierwsza = True
        for l in range(2, n//2+2):
            if n % l == 0:
                pierwsza = False
                break
        if pierwsza:
            pierwsze.append(n)

    ile_polpierwszych = 0
    najwieksza, najmniejsza = 0, 2**18
    for ciag in ciagi:
        ciag = int(str(ciag), 2)
        kopia = ciag
        for n in pierwsze:
            if ciag % n == 0 and ciag // n in pierwsze:
                ile_polpierwszych += 1
                if kopia > najwieksza:
                    najwieksza = kopia
                if kopia < najmniejsza:
                    najmniejsza = kopia
                break

    with open(r'wyniki/63/wyniki_ciagi.txt', 'a') as wyniki:
        wyniki.write(f'\n62.3\n{ile_polpierwszych} ciagow jest reprezentacja binarna liczb polpierwszych.\n'
                     f'Najwieksza z nich to {najwieksza}, a najmniejsza z nich to {najmniejsza}.')


dwucykliczne()
sasiadki()
polpierwsze()
print("--- %s seconds ---" % (time.time() - start))
