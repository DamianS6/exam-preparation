with open(r'Dane_NOWA/dane_6_1.txt') as dane:
    slowa = [__.rstrip() for __ in dane.readlines()]

with open(r'PESEL/wyniki_6_1.txt', 'w') as wyniki:
    k = 107
    for slowo in slowa:
        nowe = ''
        for litera in slowo:
            kod = (ord(litera) + k) % 65 + 26
            if kod < 65:
                kod += 52
            nowe += chr(kod)
        wyniki.write(f'{nowe}\n')