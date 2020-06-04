with open(r'Dane_NOWA/dane_6_2.txt') as dane:
    szyfry = [__.rstrip().split(' ') for __ in dane.readlines()]

with open(r'PESEL/wyniki_6_2.txt', 'w') as wyniki:
    for szyfr in szyfry:
        slowo = ''
        if len(szyfr) < 2:
            continue
        k = int(szyfr[1])
        for litera in szyfr[0]:
            kod1 = ord(litera)
            kodnowy = kod1 - k % 65 + 26
            while kodnowy < 65:
                kodnowy += 26
            if kodnowy > 90:
                kodnowy -= 26
            slowo += chr(kodnowy)
        wyniki.write(f'{slowo}\n')
