import time

start = time.time()

with open(r'dane/80/dane_trojkaty.txt') as dane:
    boki = [int(__.rstrip()) for __ in dane.readlines()]

"""
80.1.
Wypisz wszystkie trójki kolejnych liczb z pliku dane_trojkaty.txt, które są długościami
boków trójkąta prostokątnego. """


def prostokatne():
    with open(r'wyniki/80/wyniki_trojkaty.txt', 'w') as wyniki:
        wyniki.write('80.1\n')
        for n in range(len(boki) - 2):
            if boki[n]**2 == boki[n+1]**2 + boki[n+2]**2 or boki[n+1]**2 == boki[n]**2 + boki[n+2]**2 \
                    or boki[n+2] ** 2 == boki[n+1] ** 2 + boki[n] ** 2:
                wyniki.write(f"{boki[n]} {boki[n+1]} {boki[n+2]}\n")


"""
80.2.
Podaj największy obwód trójkąta, którego boki mają długości równe liczbom występującym
w różnych wierszach pliku dane_trojkaty.txt. """


def najwiekszyobwod():
    najwiekszy = 1
    for n in range(len(boki)):
        obwod = boki[n]
        for l in range(n+1, len(boki)):
            obwod = boki[n] + boki[l]
            if obwod < najwiekszy/2:
                continue
            for m in range(l+1, len(boki)):
                if boki[n] >= boki[l] + boki[m] or boki[l] >= boki[n] + boki[m] or boki[m] >= boki[l] + boki[n]:
                    continue
                obwod += boki[m]
                if obwod > najwiekszy:
                    najwiekszy = obwod
                obwod = boki[n] + boki[l]
    with open(r'wyniki/80/wyniki_trojkaty.txt', 'a') as wyniki:
        wyniki.write(f'\n80.2\n{najwiekszy}\n')


"""
80.3.
Podaj, ile nieprzystających trójkątów można utworzyć z odcinków o długościach podanych
w pliku dane_trojkaty.txt. """


def nieprzystajace():
    ile_nieprzystajacych = 0
    lista_nieprzystajacych = {}
    for n in range(len(boki)):
        for l in range(n + 1, len(boki)):
            for m in range(l + 1, len(boki)):
                if boki[n] >= boki[l] + boki[m] or boki[l] >= boki[n] + boki[m] or boki[m] >= boki[l] + boki[n]:
                    continue
                obwod = sum([boki[n], boki[l], boki[m]])
                if obwod in lista_nieprzystajacych.keys():
                    if list(lista_nieprzystajacych[obwod]) == sorted([boki[n], boki[l], boki[m]]):
                        continue
                lista_nieprzystajacych[obwod] = sorted([boki[n], boki[l], boki[m]])
                ile_nieprzystajacych += 1
    with open(r'wyniki/80/wyniki_trojkaty.txt', 'a') as wyniki:
        wyniki.write(f'\n80.3\n{ile_nieprzystajacych}\n')


prostokatne()
najwiekszyobwod()
nieprzystajace()

print(f'--- {time.time() - start} seconds ---')
