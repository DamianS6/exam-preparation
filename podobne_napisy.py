import time

start = time.time()

with open(r'dane/72/napisy.txt') as dane:
    napisy = [__.rstrip().split(' ') for __ in dane.readlines()]

"""
72.1.
Oblicz, w ilu wierszach jeden (którykolwiek) z napisów jest przynajmniej trzy razy dłuższy
od drugiego. Jako odpowiedź wypisz liczbę takich wierszy oraz parę napisów z pierwszego
z nich. """


def dluzszy():
    n = 0
    for napis in napisy:
        if len(napis[0]) >= 3*len(napis[1]) or len(napis[1]) >= 3*len(napis[0]):
            if n == 0:
                pierwszy = napis
            n += 1
    with open(r'wyniki/72/wyniki.txt', 'w') as wyniki:
        wyniki.write(f'72.1\n{n}\n')
        for n in pierwszy:
            wyniki.write(f'{n} ')


"""
72.2.
Znajdź (i wypisz) wszystkie takie wiersze pliku, w których drugi napis da się otrzymać
z pierwszego przez dopisanie na jego końcu pewnej dodatniej liczby liter (na przykład kot
i kotara). Dla każdego wiersza podaj oba znajdujące się w nim napisy, a osobno wypisz litery,
które należy dopisać. """


def dopisanie():
    with open(r'wyniki/72/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n\n72.2')
        for napis in napisy:
            if napis[0] == napis[1][:len(napis[0])]:
                wyniki.write(f'\nNapisy: {napis[0]} {napis[1]}, litery: {napis[1][len(napis[0]):]}\n')


"""
72.3.
Niektóre z podanych par napisów mają identyczne zakończenia (na przykład komputer i krater).
Znajdź i wypisz największą możliwą długość takiego zakończenia, a także wszystkie
pary napisów w wierszach, które osiągają tę maksymalną długość. """


def zakonczenia():
    najwieksza = 0
    pary = []
    for napis in napisy:
        dlugosc = 0
        koncowka = False
        for n in range(min(len(napis[0]), len(napis[1]))):
            if napis[0][::-1][n] == napis[1][::-1][n]:
                dlugosc += 1
                koncowka = True
            else:
                break
        if koncowka and dlugosc >= najwieksza:
            pary.append(napis)
            najwieksza = dlugosc

    with open(r'wyniki/72/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n72.3\nNajwieksza dlugosc: {najwieksza}\n')
        for para in pary:
            if para[0][len(para[0])-najwieksza:] == para[1][len(para[1])-najwieksza:]:
                wyniki.write(f'{para[0]} {para[1]}\n')


dluzszy()
dopisanie()
zakonczenia()

print(f'--- {time.time() - start} seconds ---')
