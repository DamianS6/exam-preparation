import time

start = time.time()

with open(r'dane/71/funkcja.txt') as dane:
    funkcje = [[] for __ in range(5)]
    n = 0
    for line in dane.readlines():
        for factor in line.split(' '):
            if len(factor) > 2:
                funkcje[n].insert(0, float(factor))
        n += 1


def oblicz_wartosc(n):
    wartosc = 0
    if n < 1:
        wartosc = n**3*funkcje[0][0] + n**2*funkcje[0][1] + n*funkcje[0][2] + funkcje[0][3]
    elif n < 2:
        wartosc = n ** 3 * funkcje[1][0] + n ** 2 * funkcje[1][1] + n * funkcje[1][2] + funkcje[1][3]
    elif n < 3:
        wartosc = n ** 3 * funkcje[2][0] + n ** 2 * funkcje[2][1] + n * funkcje[2][2] + funkcje[2][3]
    elif n < 4:
        wartosc = n ** 3 * funkcje[3][0] + n ** 2 * funkcje[3][1] + n * funkcje[3][2] + funkcje[3][3]
    elif n < 5:
        wartosc = n ** 3 * funkcje[4][0] + n ** 2 * funkcje[4][1] + n * funkcje[4][2] + funkcje[4][3]
    return wartosc


"""
71.1.
Podaj wartość f(1.5) z dokładnością do 5 cyfr po przecinku. """

with open(r'wyniki/71/wyniki_funkcja.txt', 'w') as wyniki:
    wyniki.write(f'71.1\n{str(oblicz_wartosc(1.5))[:7]}\n')


"""
71.2.
Znajdź wartość x ∈ [0,5), dla której wartość f(x) jest największa.
Jako wynik podaj wartość x z dokładnością do trzech, a wartość f(x) z dokładnością do 5
cyfr po przecinku. """


def najwieksza():
    maks = 0
    for n in range(500000):
        wartosc = oblicz_wartosc(n/100000)
        if wartosc > maks:
            maks = wartosc
            x = n/100000
    with open(r'wyniki/71/wyniki_funkcja.txt', 'a') as wyniki:
        wyniki.write(f'\n71.2\nx - {str(x)[:5]}\nf(x) - {str(maks)[:7]}\n')


"""
71.3.
Znajdź wszystkie miejsca zerowe funkcji f w przedziale [0,5). Odpowiedzi podaj z dokładnością
do 5 cyfr po przecinku. """


def miejsca_zerowe():
    with open(r'wyniki/71/wyniki_funkcja.txt', 'a') as wyniki:
        wyniki.write(f'\n71.3\n')
    for n in range(5000000):
        if oblicz_wartosc(n / 1000000) > 0 > oblicz_wartosc((n + 1) / 1000000) or \
                oblicz_wartosc(n / 1000000) < 0 < oblicz_wartosc((n + 1) / 1000000):
            print(n/1000000, oblicz_wartosc(n / 1000000), (n+1)/1000000, oblicz_wartosc((n+1) / 1000000))
            with open(r'wyniki/71/wyniki_funkcja.txt', 'a') as wyniki:
                wyniki.write(f'{str(n/1000000)[:7]}\n')


najwieksza()
miejsca_zerowe()

print(f'--- {time.time() - start} seconds ---')
