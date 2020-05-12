import time

start = time.time()

with open(r'dane/73/tekst.txt') as dane:
    tekst = [__.rstrip() for __ in dane.read().split(' ')]

"""
73.1.
Oblicz, ile jest w tekście słów, w których występują dwie kolejne takie same litery. """


def kolejne():
    powtorzenia = 0
    for slowo in tekst:
        for n in range(len(slowo)-1):
            if slowo[n] == slowo[n+1]:
                powtorzenia += 1
                break

    with open(r'wyniki/73/wyniki.txt', 'w') as wyniki:
        wyniki.write(f'73.1\n{powtorzenia}\n\n73.2\n')


"""
73.2.
Sporządź statystykę częstotliwości występowania liter w tekście: dla każdej litery podaj liczbę
jej wystąpień we wszystkich słowach tekstu oraz jej procentowy udział wśród wystąpień
wszystkich liter w tekście(do statystyki nie wliczaj spacji). Odpowiedź zapisz w następującej
postaci:
A: 632 (7.56%)
B: 196 (2.34%)
...
Wartości procentowe podaj w zaokrągleniu do dwóch miejsc po przecinku. """


def czestotliwosc():
    wystepowanie = {}
    for slowo in tekst:
        for litera in slowo:
            if litera not in wystepowanie.keys():
                wystepowanie[litera] = 1
            else:
                wystepowanie[litera] += 1
    wszystkie = sum(wystepowanie.values())

    with open(r'wyniki/73/wyniki.txt', 'a') as wyniki:
        for litera in sorted(wystepowanie.items()):
            wyniki.write(f'{litera[0]} {litera[1]} ({(litera[1]/wszystkie*100).__round__(2)}%)\n')


"""
73.3.
Wśród słów w tekście policz długość najdłuższego podsłowa (fragmentu złożonego z kolejnych
liter) złożonego z samych spółgłosek. Pamiętaj, że samogłoski to: A, E, I, O, U oraz Y,
zaś pozostałe litery są spółgłoskami.
Podaj długość najdłuższego takiego podsłowa, liczbę słów, które zawierają podsłowo o takiej
długości, oraz pierwsze z nich, które występuje w pliku tekst.txt. """


def najdluzsze_podslowo():
    samogloski = ['A', 'E', 'I', 'O', 'U', 'Y']
    najdluzsze = 1
    podslowa = []
    for slowo in tekst:
        podslowo = ''
        dlugosc = 1

        for n in range(len(slowo)-1):
            if slowo[n] not in samogloski and slowo[n+1] not in samogloski:
                podslowo += slowo[n]
                dlugosc += 1
            else:
                if dlugosc >= najdluzsze:
                    najdluzsze = dlugosc
                    podslowa.append(podslowo + slowo[n])
                dlugosc = 1
                podslowo = ''

    for podslowo in podslowa[:]:
        if len(podslowo) < najdluzsze:
            podslowa.remove(podslowo)

    for slowo in tekst:
        if podslowa[0] in slowo:
            pierwsze = slowo
            break

    with open(r'wyniki/73/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n73.3\nDlugosc: {najdluzsze}\nLiczba slow: {len(podslowa)}\nPierwsze: {pierwsze}')


kolejne()
czestotliwosc()
najdluzsze_podslowo()

print(f'--- {time.time() - start} seconds ---')
