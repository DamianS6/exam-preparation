with open(r'Dane_NOWA/dane_6_3.txt') as dane:
    szyfry = [__.rstrip().split(' ') for __ in dane.readlines()]

with open(r'PESEL/wyniki_6_3.txt', 'w') as wyniki:
    for szyfr in szyfry:
        slowo = ''
        k = ord(szyfr[0][0])%26 - ord(szyfr[1][0])%26
        if k < 0:
            k += 26
        for litera in szyfr[0]:
            kod1 = ord(litera)
            kodnowy = kod1 - k % 65 + 26
            while kodnowy < 65:
                kodnowy += 26
            if kodnowy > 90:
                kodnowy -= 26
            slowo += chr(kodnowy)
        if szyfr[1] != slowo:
            wyniki.write(f'{szyfr[0]}\n')
