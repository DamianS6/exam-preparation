with open(r'dane/76/szyfr1.txt') as dane:
    zestaw1 = [__.rstrip() for __ in dane.readlines()]
    szyfr1 = list(zestaw1.pop(6).split(' '))

with open(r'dane/76/szyfr2.txt') as dane:
    zestaw2 = [__.rstrip() for __ in dane.readlines()]
    szyfr2 = list(zestaw2.pop(1).split(' '))

with open(r'dane/76/szyfr3.txt') as dane:
    zaszyfrowane = dane.read()

"""
76.1.
W pliku szyfr1.txt dane są:
• w wierszach o numerach od 1 do 6 — napisy złożone z 50 liter alfabetu łacińskiego;
• w wierszu nr 7 — klucz 50-elementowy; liczby oddzielone są pojedynczym odstępem.
Zaszyfruj wszystkie sześć napisów zgodnie z opisaną metodą. Wynik, czyli zaszyfrowane
napisy, zapisz w osobnych wierszach w pliku wyniki_szyfr1.txt.

76.2.
W pliku szyfr2.txt dane są:
• w pierwszym wierszu — napis złożony z 50 liter alfabetu łacińskiego;
• w drugim wierszu — klucz 15-elementowy; liczby oddzielone są pojedynczym odstępem.
Zaszyfruj dany napis zgodnie z opisaną metodą. Wynik, czyli zaszyfrowany napis, zapisz
w pliku wyniki_szyfr2.txt."""


def szyfrowanie():
    with open(r'wyniki/76/wyniki_szyfr1.txt', 'w') as wyniki:
        for napis in zestaw1:
            napis = list(napis)
            for n in range(len(napis)):
                napis[n], napis[int(szyfr1[n])-1] = napis[int(szyfr1[n])-1], napis[n]
            wyniki.write(f"{''.join(napis)}\n")

    napis = list(zestaw2[0])
    szyfr2.extend(szyfr2*10)
    for n in range(len(napis)):
        napis[n], napis[int(szyfr2[n])-1] = napis[int(szyfr2[n])-1], napis[n]
    with open(r'wyniki/76/wyniki_szyfr2.txt', 'w') as wyniki:
        wyniki.write(''.join(napis))


"""
76.3.
W pliku szyfr3.txt dany jest napis złożony z 50 liter alfabetu łacińskiego. Napis ten powstał
po zaszyfrowaniu pewnego napisu A kluczem [6, 2, 4, 1, 5, 3].
2. Zadania praktyczne rozwiązywane z użyciem komputera 139
Podaj napis A. Wynik zapisz w pliku wyniki_szyfr3.txt. """


def deszyfrowanie():
    szyfr3 = [6, 2, 4, 1, 5, 3]*10
    napis = list(zaszyfrowane)
    for n in range(49, -1, -1):
        napis[n], napis[szyfr3[n]-1] = napis[szyfr3[n]-1], napis[n]
    with open(r'wyniki/76/wyniki_szyfr3.txt', 'w') as wyniki:
        wyniki.write(''.join(napis))


szyfrowanie()
deszyfrowanie()
