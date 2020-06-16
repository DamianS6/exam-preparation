with open(r'Arkusze/Probna_2020/festyn.txt') as dane:
    dane = [_.rstrip() for _ in dane.readlines()]

zestaw1 = [dane[0], dane[1:64], dane[64], dane[65:89]]
tarcze1, strzaly1 = zestaw1[1], zestaw1[3]

zestaw2 = [dane[89], dane[90:146], dane[146], dane[147:158]]
tarcze2, strzaly2 = zestaw2[1], zestaw2[3]

zestaw3 = [dane[158], dane[159:241], dane[241], dane[242:]]
tarcze3, strzaly3 = zestaw3[1], zestaw3[3]


# 4.1
def punkty():
    with open(r'Arkusze/Probna_2020/zadnie4.txt', 'w') as wyniki:
        wyniki.write(f'4.1\n')
        pkty = 0
        for tarcza in tarcze1:
            tarcza = tarcza.split()
            c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
            for strzal in strzaly1:
                if c1 <= int(strzal) <= c2:
                    pkty += 1
                    break
        wyniki.write(f"Dla zestawu pierwszego Jas uzyskal {pkty} punktow.\n")
        pkty = 0
        for tarcza in tarcze2:
            tarcza = tarcza.split()
            c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
            for strzal in strzaly2:
                if c1 <= int(strzal) <= c2:
                    pkty += 1
                    break
        wyniki.write(f"Dla zestawu drugiego Jas uzyskal {pkty} punktow.\n")
        pkty = 0
        for tarcza in tarcze3:
            tarcza = tarcza.split()
            c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
            for strzal in strzaly3:
                if c1 <= int(strzal) <= c2:
                    pkty += 1
                    break
        wyniki.write(f"Dla zestawu trzeciego Jas uzyskal {pkty} punktow.\n")


# 4.2
def maks_czas():
    with open(r'Arkusze/Probna_2020/zadnie4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.2\n')
        maks = 0
        for tarcza in tarcze1:
            tarcza = tarcza.split()
            czas = int(tarcza[1])
            if czas > maks:
                maks = czas
        wyniki.write(f'Pierwszy zestaw: {maks} sekund.\n')
        maks = 0
        for tarcza in tarcze2:
            tarcza = tarcza.split()
            czas = int(tarcza[1])
            if czas > maks:
                maks = czas
        wyniki.write(f'Drugi zestaw: {maks} sekund.\n')
        maks = 0
        for tarcza in tarcze3:
            tarcza = tarcza.split()
            czas = int(tarcza[1])
            if czas > maks:
                maks = czas
        wyniki.write(f'Trzeci zestaw: {maks} sekund.\n')


# 4.3
def sekunda():
    with open(r'Arkusze/Probna_2020/zadnie4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.3\n')
        najlepsza, najwiecej = 0, 0
        for strzal in strzaly1:
            pkty = 0
            for tarcza in tarcze1:
                tarcza = tarcza.split()
                c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
                if c1 <= int(strzal) <= c2:
                    pkty += 1
            if pkty > najwiecej:
                najlepsza = int(strzal)
                najwiecej = pkty
        wyniki.write(f'Pierwszy zestaw: {najlepsza} sekunda.\n')
        najlepsza, najwiecej = 0, 0
        for strzal in strzaly2:
            pkty = 0
            for tarcza in tarcze2:
                tarcza = tarcza.split()
                c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
                if c1 <= int(strzal) <= c2:
                    pkty += 1
            if pkty > najwiecej:
                najlepsza = int(strzal)
                najwiecej = pkty
        wyniki.write(f'Drugi zestaw: {najlepsza} sekunda.\n')
        najlepsza, najwiecej = 0, 0
        for strzal in strzaly3:
            pkty = 0
            for tarcza in tarcze3:
                tarcza = tarcza.split()
                c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
                if c1 <= int(strzal) <= c2:
                    pkty += 1
            if pkty > najwiecej:
                najlepsza = int(strzal)
                najwiecej = pkty
        wyniki.write(f'Trzeci zestaw: {najlepsza} sekunda.\n')


# 4.4
def gdyby():
    with open(r'Arkusze/Probna_2020/zadnie4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.4\n')
        pkty = 0
        for strzal in strzaly1:
            for tarcza in tarcze1:
                tarcza = tarcza.split()
                c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
                if c1 <= int(strzal) <= c2:
                    pkty += 1
        wyniki.write(f"Dla zestawu pierwszego Jas uzyskalby {pkty} punktow.\n")
        pkty = 0
        for strzal in strzaly2:
            for tarcza in tarcze2:
                tarcza = tarcza.split()
                c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
                if c1 <= int(strzal) <= c2:
                    pkty += 1
        wyniki.write(f"Dla zestawu drugiego Jas uzyskalby {pkty} punktow.\n")
        pkty = 0
        for strzal in strzaly3:
            for tarcza in tarcze3:
                tarcza = tarcza.split()
                c1, c2 = int(tarcza[0]), int(tarcza[0]) + int(tarcza[1])
                if c1 <= int(strzal) <= c2:
                    pkty += 1
        wyniki.write(f"Dla zestawu trzeciego Jas uzyskalby {pkty} punktow.\n")


punkty()
maks_czas()
sekunda()
gdyby()
