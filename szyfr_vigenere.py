with open(r'dane/77/dokad.txt') as dane:
    dokad = ''.join(dane.readlines())

with open(r'dane/77/szyfr.txt') as dane:
    szyfr = dane.read().rstrip().split('\n')
    klucz1 = szyfr.pop(1)*500
    szyfr = szyfr[0]

tabela = {}
i = 0
for z in 'abcdefghijklmnopqrstuvwxyz'.upper():
    tabela[z] = i
    i += 1

"""
77.1.
W pliku dokad.txt znajduje się jeden wiersz z tekstem. Długość tekstu nie przekracza
1024 znaków. Należy zaszyfrować ten tekst metodą Vigenère’a, używając jako klucza słowa:
”LUBIMYCZYTAC”.
a) Podaj liczbę powtórzeń klucza niezbędną do zaszyfrowania całego tekstu źródłowego
(uwzględniając w nich ostatnie rozpoczęte powtórzenie).
b) Podaj zaszyfrowany tekst i zapisz go w pliku z odpowiedziami. """


def szyfrowanie():
    klucz = 'LUBIMYCZYTAC'*50
    zaszyfrowany = []
    k = 0
    for n in range(len(dokad)):
        if dokad[n] in [' ', ',', '.']:
            zaszyfrowany.append(dokad[n])
        else:
            kod = (tabela[dokad[n]] + tabela[klucz[k]]) % 26
            k += 1
            zaszyfrowany.append(list(tabela.keys())[list(tabela.values()).index(kod)])
    with open(r'wyniki/77/Vigenere_wyniki.txt', 'w') as wyniki:
        wyniki.write(f"77.1\n"
                     f"{int(len(dokad.replace(' ', '').replace(',', '').replace('.', ''))/len('lubimyczytac'))+1}\n"
                     f"{''.join(zaszyfrowany)}\n")


"""
W pliku szyfr.txt zapisano dwa wiersze. W pierwszym wierszu znajduje się tekst zaszyfrowany
metodą Vigenère’a. W drugim wierszu znajduje się klucz użyty do tego szyfrowania.
140 Egzamin maturalny. Informatyka. Poziom rozszerzony. Zbiór zadań
Szyfr zawiera wiele słów. Jego łączna długość nie przekracza 1024 znaków. Szyfrowaniu
podlegały tylko wielkie litery tekstu, zaś odstępy i znaki przestankowe pozostały bez zmiany.
Odszyfruj tekst i umieść jego postać źródłową w pliku z odpowiedziami. """


def rozszyfrowanie():
    rozszyfrowany = []
    k = 0
    for n in range(len(szyfr)):
        if szyfr[n] in [' ', ',', '.']:
            rozszyfrowany.append(szyfr[n])
        else:
            kod = (tabela[szyfr[n]] - tabela[klucz1[k]]) % 26
            k += 1
            rozszyfrowany.append(list(tabela.keys())[list(tabela.values()).index(kod)])
    with open(r'wyniki/77/Vigenere_wyniki.txt', 'a') as wyniki:
        wyniki.write(f"\n77.2\n{''.join(rozszyfrowany)}\n")


"""
Podaj liczby wystąpień poszczególnych liter A, B, ..., Z w treści szyfru zawartego
w pierwszym wierszu pliku szyfr.txt. 
Chcąc złamać szyfr Vigenère, nie znając klucza, w pierwszym kroku należy oszacować
długość klucza (rozumianą jako liczba znaków).
[...]
Wykorzystując powyższe wzory, wyznacz szacunkową długość klucza dla szyfru danego
w pierwszym wierszu pliku szyfr.txt i porównaj z dokładną długością klucza umieszczonego
w drugim wierszu tego pliku. Wypisz obie wartości, wartość szacunkową zaokrąglij
do 2 cyfr po przecinku. """


def lamanie():
    wystapienia = {}
    for letter in szyfr:
        if letter in [' ', ',', '.']:
            continue
        if letter in wystapienia:
            wystapienia[letter] += 1
        else:
            wystapienia[letter] = 1

    indeks = 0
    for val in wystapienia.values():
        indeks += val*(val-1)
    indeks /= sum(wystapienia.values()) * (sum(wystapienia.values())-1)
    dlugosc = 0.0285 / (indeks - 0.0385)
    with open(r'wyniki/77/Vigenere_wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n77.3\nLiczby wystapien:\n')
        for key, value in sorted(wystapienia.items()):
            wyniki.write(f'{key}: {value}\n')
        wyniki.write(f'\nSzacunkowa dlugosc: {round(dlugosc, 2)}\nDokladna dlugosc: {len(klucz1)//500}')


szyfrowanie()
rozszyfrowanie()
lamanie()
