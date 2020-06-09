with open(r'Arkusze/Maj_2018/sygnaly.txt') as dane:
    sygnaly = [__.rstrip() for __ in dane.readlines()]


# 4.1.
def przeslanie():
    przesl = ''
    for n in sygnaly[39::40]:
        przesl += n[9]
    with open(r'Arkusze/Maj_2018/wyniki4.txt', 'w') as wyniki:
        wyniki.write(f'4.1.\n{przesl}\n')


# 4.2.
def najwiecej_roznych():
    ile = 0
    rozne = []
    najwieksze = ''
    for sygnal in sygnaly:
        potencjalny = []
        if len(sygnal) < len(rozne):
            continue
        for litera in sygnal:
            if litera not in potencjalny:
                potencjalny.append(litera)
        if len(potencjalny) > len(rozne):
            najwieksze = sygnal
            rozne = potencjalny
            ile = len(rozne)
    with open(r'Arkusze/Maj_2018/wyniki4.txt', 'a') as wyniki:
        wyniki.write(f"\n4.2.\n{najwieksze} {ile}\n")


# 4.3.
def oddalone():
    with open(r'Arkusze/Maj_2018/wyniki4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.3.')
        for sygnal in sygnaly:
            bliskie = True
            for litera in sygnal:
                for litera2 in sygnal:
                    if abs(ord(litera) - ord(litera2)) > 10:
                        bliskie = False
                        break
            if bliskie:
                wyniki.write(f'\n{sygnal}')


przeslanie()
najwiecej_roznych()
oddalone()
