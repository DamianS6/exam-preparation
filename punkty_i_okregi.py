with open(r'Arkusze/Probna_2017/okregi.txt') as dane:
    tym_okregi = [__.rstrip().split() for __ in dane.readlines()]

okregi = []
for asd in tym_okregi:
    nowy = [int(__) for __ in asd]
    okregi.append(nowy)

with open(r'Arkusze/Probna_2017/punkty.txt') as dane:
    punkty = [__.rstrip().split() for __ in dane.readlines()]


# 4.1
def cwiartki():
    pierwsza, druga, trzecia, czwarta = 0, 0, 0, 0
    for punkt in punkty:
        if float(punkt[0]) > 0 and float(punkt[1]) > 0:
            pierwsza += 1
        elif float(punkt[0]) < 0 < float(punkt[1]):
            druga += 1
        elif float(punkt[0]) < 0 and float(punkt[1]) < 0:
            trzecia += 1
        else:
            czwarta += 1
    with open(r'Arkusze/Probna_2017/wynik1.txt', 'w') as wynik:
        wynik.write(f'{pierwsza} {druga} {trzecia} {czwarta}')


# 4.2
def styczne():
    liczba = 0
    lista = []
    for okrag in okregi:
        if okrag[1] == okrag[2] or okrag[1] == okrag[2]*(-1):
            liczba += 1
            lista.append([okrag[0], okrag[1], okrag[2]])
    for n in range(len(lista)):
        for s in range(len(lista)):
            if lista[n][0] < lista[s][0]:
                lista[n], lista[s] = lista[s], lista[n]
            if lista[n][0] == lista[s][0]:
                if lista[n][1] < lista[s][1]:
                    lista[n], lista[s] = lista[s], lista[n]
    with open(r'Arkusze/Probna_2017/wynik2.txt', 'w') as wynik:
        for okrag in lista:
            wynik.write(f'{okrag[0]} {okrag[1]} {okrag[2]}\n')
        wynik.write(str(liczba))


# 4.3
def wielokat():
    pole = 0
    for n in range(len(punkty)-1):
        xa, ya = float(punkty[n][0]), float(punkty[n][1])
        xb, yb = float(punkty[n+1][0]), float(punkty[n+1][1])
        xc, yc = 0, 0
        male_pole = 1/2 * abs(xa*yb + xb*yc + xc*ya - xc*yb - xa*yc - xb*ya)
        pole += male_pole
    xa, ya = float(punkty[-1][0]), float(punkty[-1][1])
    xb, yb = float(punkty[0][0]), float(punkty[0][1])
    xc, yc = 0, 0
    pole += 1/2 * abs(xa*yb + xb*yc + xc*ya - xc*yb - xa*yc - xb*ya)
    with open(r'Arkusze/Probna_2017/wynik3.txt', 'w') as wynik:
        wynik.write(str(int(pole)))


cwiartki()
styczne()
wielokat()
