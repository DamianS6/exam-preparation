with open(r'Arkusze/Probna_2016/dane.txt') as dane:
    okregi = [__.rstrip().split() for __ in dane.readlines()]


# 4.1.
def najkrotszy():
    with open(r'Arkusze/Probna_2016/wynik1.txt', 'w') as wynik:
        promien = int(okregi[0][2])
        for okrag in okregi:
            if int(okrag[2]) < promien:
                promien = int(okrag[2])
        for okrag in okregi:
            if int(okrag[2]) == promien:
                for s in okrag:
                    wynik.write(f'{s} ')
                wynik.write('\n')


# 4.2.
def wnetrze():
    najwiecej = 0
    najx, najy, najr = int(okregi[0][0]), int(okregi[0][1]), int(okregi[0][2])
    for okrag in okregi:
        r = int(okrag[2])
        x1, y1 = int(okrag[0]), int(okrag[1])
        ile = 0
        for okrag2 in okregi:
            if okrag == okrag2:
                continue
            x2, y2 = int(okrag2[0]), int(okrag2[1])
            if ((x2-x1)**2 + (y2-y1)**2)**(1/2) <= r:
                ile += 1
        if ile > najwiecej:
            najx, najy, najr = x1, y1, r
            najwiecej = ile
    with open(r'Arkusze/Probna_2016/wynik2.txt', 'w') as wynik:
        wynik.write(f'{najx} {najy} {najr}\n{najwiecej}')


# 4.3.
def styczne():
    lista = []
    ile = 0
    for okrag in okregi:
        x1, y1, r1 = int(okrag[0]), int(okrag[1]), int(okrag[2])
        for okrag2 in okregi:
            if okrag == okrag2:
                continue
            x2, y2, r2 = int(okrag2[0]), int(okrag2[1]), int(okrag2[2])
            if ((x2-x1)**2 + (y2-y1)**2)**(1/2) == r1 + r2 or ((x2-x1)**2 + (y2-y1)**2)**(1/2) == abs(r1 - r2):
                lista.append([x1, y1, r1, x2, y2, r2])
                ile += 1
    with open(r'Arkusze/Probna_2016/wynik3.txt', 'w') as wynik:
        wynik.write(str(ile))
        for styczny in lista:
            wynik.write('\n')
            for cyfra in styczny:
                wynik.write(f'{cyfra} ')


najkrotszy()
wnetrze()
styczne()
