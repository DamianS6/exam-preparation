with open(r'Arkusze/Czerwiec_2017/punkty.txt') as dane:
    punkty1 = [__.rstrip().split(' ') for __ in dane.readlines()]

punkty = []

for __ in punkty1:
    punktt = []
    for ___ in __:
        punkt = int(___)
        punktt.append(punkt)
    punkty.append(punktt)


pierwsze = [2]


def lista_pierwszych():
    for i in range(3, 10000):
        pierwsza = True
        for s in range(2, int(i/2)):
            if i % s == 0:
                pierwsza = False
                break
        if pierwsza and i not in pierwsze:
            pierwsze.append(i)


# 4.1.
def ile_pierwszych():
    ile = 0
    for n in punkty:
        if n[0] in pierwsze and n[1] in pierwsze:
            ile += 1
    with open(r'Arkusze/Czerwiec_2017/wyniki4.txt', 'w') as wyniki:
        wyniki.write(f'4.1.\n{ile}\n')


# 4.2.
def cyfropodobne():
    ile = 0
    for n in punkty:
        cyfropod = True
        for s in range(0, 9):
            if str(s) in str(n[0]) and str(s) not in str(n[1]) or str(s) in str(n[1]) and str(s) not in str(n[0]):
                cyfropod = False
                break
        if cyfropod:
            ile += 1
    with open(r'Arkusze/Czerwiec_2017/wyniki4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.2.\n{ile}\n')


# 4.3.
def oddalone():
    x1, y1, x2, y2, odl = 0, 0, 0, 0, 0
    for n in punkty:
        for s in punkty:
            if ((s[0]-n[0])**2 + (s[1]-n[1])**2)**(1/2) > odl:
                odl = ((s[0]-n[0])**2 + (s[1]-n[1])**2)**(1/2)
                x1, y1, x2, y2 = n[0], n[1], s[0], s[1]
    with open(r'Arkusze/Czerwiec_2017/wyniki4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.3.\nA({x1}, {y1})\nB({x2}, {y2})\nOdleglosc: {round(odl)}\n')


# 4.4.
def kwadrat():
    wewnatrz, boki, zewnatrz = 0, 0, 0
    for n in punkty:
        if n[0] < 5000 and n[1] < 5000:
            wewnatrz += 1
        elif n[0] == 5000 or n[1] == 5000:
            boki += 1
        else:
            zewnatrz += 1
    with open(r'Arkusze/Czerwiec_2017/wyniki4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.4.\nWewnatrz: {wewnatrz}\nNa bokach: {boki}\nNa zewnatrz: {zewnatrz}')


lista_pierwszych()
ile_pierwszych()
cyfropodobne()
oddalone()
kwadrat()
