import time
start = time.time()

with open(r'dane/66/trojki.txt') as dane:
    trojki = []
    for l in dane.readlines():
        trojki.append(l.rstrip().split(' '))
    for l in range(len(trojki)):
        for __ in range(3):
            trojki[l][__] = int(trojki[l][__])


with open(r'wyniki/66/wyniki.trojki.txt', 'w') as wyniki:
    wyniki.write('66.1\n')


"""
66.1 Wypisz wszystkie trójki liczb z pliku trojki.txt, w których suma cyfr dwóch pierwszych
liczb jest równa ostatniej (trzeciej) liczbie. """


def czy_suma():
    for tr in trojki:
        suma = 0
        for n in tr[:2]:
            for cyfra in str(n):
                suma += int(cyfra)
        if suma == tr[2]:
            with open(r'wyniki/66/wyniki.trojki.txt', 'a') as wyniki:
                for n in tr:
                    wyniki.write(f'{str(n)} ')
                wyniki.write('\n')


"""
66.2.
Wypisz wszystkie wiersze z pliku trojki.txt zawierające takie trzy liczby a, b, c, w których
a i b są liczbami pierwszymi oraz c = a · b. """


def pierwsza(x):
    return all(x % i for i in range(2, x))


def pierwsze_iloczyn():
    with open(r'wyniki/66/wyniki.trojki.txt', 'a') as wyniki:
        wyniki.write('\n66.2\n')
    for tr in trojki:
        if tr[0] * tr[1] == tr[2]:
            if pierwsza(tr[0]) and pierwsza(tr[1]):
                with open(r'wyniki/66/wyniki.trojki.txt', 'a') as wyniki:
                    for n in tr:
                        wyniki.write(f'{str(n)} ')
                    wyniki.write('\n')


"""
66.3.
Wypisz z pliku trojki.txt wszystkie pary sąsiadujących ze sobą wierszy, takie że liczby
w tych wierszach są długościami boków trójkątów prostokątnych. """


def prostokatny(tr):
    return tr[0]**2 + tr[1]**2 == tr[2]**2 or tr[1]**2 + tr[2]**2 == tr[0]**2 or tr[0]**2 + tr[2]**2 == tr[1]**2


def prostokatne():
    with open(r'wyniki/66/wyniki.trojki.txt', 'a') as wyniki:
        wyniki.write('\n66.3\n')
    for tr in range(len(trojki)):
        if prostokatny(trojki[tr]) and prostokatny(trojki[tr+1]):
            with open(r'wyniki/66/wyniki.trojki.txt', 'a') as wyniki:
                for n in trojki[tr]:
                    wyniki.write(f'{str(n)} ')
                wyniki.write('\n')
                for n in trojki[tr+1]:
                    wyniki.write(f'{str(n)} ')
                wyniki.write('\n\n')


"""
66.4.
Podaj, ile jest w pliku trojki.txt wierszy, w których znajdują się liczby reprezentujące
długości boków trójkąta. Ciąg wierszy nazywamy trójkątnym, jeśli liczby w każdym wierszu
reprezentują długości boków trójkąta. Podaj długość najdłuższego ciągu trójkątnego w pliku. """


def nietrojkatny(ciag):
    return ciag[0] >= ciag[1] + ciag[2] or ciag[1] >= ciag[0] + ciag[2] or ciag[2] >= ciag[0] + ciag[1]


def trojkatne():
    dlugosc = 0
    najdluzszy = 1
    ile = 0
    for tr in trojki:
        if not nietrojkatny(tr):
            ile += 1
            dlugosc += 1
        if nietrojkatny(tr):
            if dlugosc > najdluzszy:
                najdluzszy = dlugosc
            dlugosc = 0
    with open(r'wyniki/66/wyniki.trojki.txt', 'a') as wyniki:
        wyniki.write(f'66.4\n{ile} wierszy.\n{najdluzszy} - dlugosc najdluzszego ciagu.')



czy_suma()
pierwsze_iloczyn()
prostokatne()
trojkatne()

print(' --- %s seconds --- ' % (time.time() - start))
