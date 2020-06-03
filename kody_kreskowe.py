with open(r'Arkusze/Czerwiec_2015/dane/kody.txt') as dane:
    kody = [__.rstrip() for __ in dane.readlines()]

kody_cyfr = {0: 10101110111010,
             1: 11101010101110,
             2: 10111010101110,
             3: 11101110101010,
             4: 10101110101110,
             5: 11101011101010,
             6: 10111011101010,
             7: 10101011101110,
             8: 11101010111010,
             9: 10111010111010}

start, stop = '11011010', '11010110'

with open(r'Arkusze/Czerwiec_2015/PESEL/kody1.txt', 'w') as wyniki:
    wyniki.write('')
with open(r'Arkusze/Czerwiec_2015/PESEL/kody2.txt', 'w') as wyniki:
    wyniki.write('')
with open(r'Arkusze/Czerwiec_2015/PESEL/kody3.txt', 'w') as wyniki:
    wyniki.write('')

for n in kody:

    kod_kreskowy = start
    nn = n[::-1]

    # 6.1.
    suma_parzystych, suma_nieparzystych = 0, 0
    for pozycja in range(len(n)):
        if pozycja % 2 == 0:
            suma_parzystych += int(nn[pozycja])
        else:
            suma_nieparzystych += int(nn[pozycja])

        kod_kreskowy += str(kody_cyfr[int(n[pozycja])])

    # 6.2.
    cyfra_kontrolna = (10 - ((suma_parzystych * 3 + suma_nieparzystych) % 10)) % 10
    kod_kontrolny = kody_cyfr[cyfra_kontrolna]

    # 6.3.
    kod_kreskowy += str(kod_kontrolny)
    kod_kreskowy += stop

    with open(r'Arkusze/Czerwiec_2015/PESEL/kody1.txt', 'a') as wyniki:
        wyniki.write(f'{suma_parzystych} {suma_nieparzystych}\n')

    with open(r'Arkusze/Czerwiec_2015/PESEL/kody2.txt', 'a') as wyniki:
        wyniki.write(f'{cyfra_kontrolna} {kod_kontrolny}\n')

    with open(r'Arkusze/Czerwiec_2015/PESEL/kody3.txt', 'a') as wyniki:
        wyniki.write(f'{kod_kreskowy}\n')
