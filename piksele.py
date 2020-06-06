with open(r'Arkusze/Maj_2017/dane.txt') as dane:
    tymcz = [__.rstrip().split() for __ in dane.readlines()]

obraz = []


def zamien_na_int():
    for l in tymcz:
        nowa = []
        for liczba in l:
            nowa.append(int(liczba))
        obraz.append(nowa)


# 6.1.
def naj():
    najciemniejszy = 255
    najjasniejszy = 0
    for wiersz in obraz:
        for liczba in wiersz:
            if int(liczba) > najjasniejszy:
                najjasniejszy = int(liczba)
            if int(liczba) < najciemniejszy:
                najciemniejszy = int(liczba)
    with open(r'Arkusze/Maj_2017/wyniki6.txt', 'w') as wyniki:
        wyniki.write(f'6.1.\nNajjasniejszy: {najjasniejszy}\nNajciemniejszy: {najciemniejszy}\n')


# 6.2.
def symetria():
    ile = 0
    for wiersz in obraz:
        for n in range(160):
            if wiersz[n] != wiersz[-(n+1)]:
                ile += 1
                break
    with open(r'Arkusze/Maj_2017/wyniki6.txt', 'a') as wyniki:
        wyniki.write(f'\n6.2.\n{ile}\n')


# 6.3.
def kontrast():
    ile = 0
    for r in range(200):

        if r == 0:
            for p in range(320):
                if p == 0 and (abs([r][p] - obraz[r][p+1]) > 128 or abs([r][p] - obraz[r+1][p]) > 128):
                    ile += 1
                elif p == 319 and (abs(obraz[r][p] - obraz[r][p-1]) > 128 or abs(obraz[r][p] - obraz[r+1][p]) > 128):
                    ile += 1
                elif p != 0 and p != 319:
                    if abs(obraz[r][p] - obraz[r][p+1]) > 128 or abs(obraz[r][p] - obraz[r+1][p]) > 128 or\
                            abs(obraz[r][p] - obraz[r][p-1]) > 128:
                        ile += 1

        elif r == 199:
            for p in range(320):
                if p == 0 and (abs(obraz[r][p] - obraz[r][p+1]) > 128 or abs(obraz[r][p] - obraz[r-1][p]) > 128):
                    ile += 1
                elif p == 319 and (abs(obraz[r][p] - obraz[r][p-1]) > 128 or abs(obraz[r][p] - obraz[r-1][p-1]) > 128):
                    ile += 1
                elif p != 0 and p != 319:
                    if abs(obraz[r][p] - obraz[r][p+1]) > 128 or abs(obraz[r][p] - obraz[r-1][p]) > 128 or\
                            abs(obraz[r][p] - obraz[r][p-1]) > 128:
                        ile += 1

        else:
            for p in range(320):
                if p == 0 and (abs(obraz[r][p] - obraz[r][p+1]) > 128 or abs(obraz[r][p] - obraz[r+1][p]) > 128 or
                               abs(obraz[r][p] - obraz[r-1][p]) > 128):
                    ile += 1
                elif p == 319 and (abs(obraz[r][p] - obraz[r][p-1]) > 128 or abs(obraz[r][p] - obraz[r+1][p]) > 128 or
                        abs(obraz[r][p] - obraz[r-1][p]) > 128):
                    ile += 1
                elif p != 0 and p != 319:
                    if abs(obraz[r][p] - obraz[r][p+1]) > 128 or abs(obraz[r][p] - obraz[r+1][p]) > 128 or\
                            abs(obraz[r][p] - obraz[r][p-1]) > 128 or abs(obraz[r][p] - obraz[r-1][p]) > 128:
                        ile += 1

    with open(r'Arkusze/Maj_2017/wyniki6.txt', 'a') as wyniki:
        wyniki.write(f'\n6.3.\n{ile}\n')


# 6.4.
def pionowa():
    pionowe = []
    for k in range(320):
        nowa = []
        for w in range(200):
            nowa.append(obraz[w][k])
        pionowe.append(nowa)

    najdluzsza = 1
    for kolumna in pionowe:
        dlugosc = 1
        for n in range(len(kolumna)-1):
            if kolumna[n] == kolumna[n+1]:
                dlugosc += 1
            else:
                if dlugosc > najdluzsza:
                    najdluzsza = dlugosc
                dlugosc = 1
    with open(r'Arkusze/Maj_2017/wyniki6.txt', 'a') as wyniki:
        wyniki.write(f'\n6.4.\n{najdluzsza}')


zamien_na_int()
naj()
symetria()
kontrast()
pionowa()
