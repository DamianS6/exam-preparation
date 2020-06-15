with open(r'Arkusze/Probna_2019/plansza.txt') as dane:
    plansza = [_.rstrip().split() for _ in dane.readlines()]

with open(r'Arkusze/Probna_2019/robot.txt') as dane:
    roboty = [_.rstrip() for _ in dane.readlines()]


# 4.1
def dyskwalifikacja():
    ile = 0
    for robot in roboty:
        prawo, dol = 0, 0
        for ruch in robot:
            if ruch == 'E':
                prawo += 1
            elif ruch == 'N':
                dol -= 1
            elif ruch == 'S':
                dol += 1
            elif ruch == 'W':
                prawo -= 1
            if prawo < 0 or dol < 0 or prawo > 19 or dol > 19:
                ile += 1
                break
    with open(r'Arkusze/Probna_2019/zadanie4.txt', 'w') as wyniki:
        wyniki.write(f'4.1\n{ile}\n')


# 4.2
def punkty():
    numer_wiersza = 0
    max_numer = 0
    max_punkty = 0
    for robot in roboty:
        numer_wiersza += 1
        p, d = 0, 0
        pkty = 3
        for ruch in robot:
            if ruch == 'E':
                p += 1
            elif ruch == 'N':
                d -= 1
            elif ruch == 'S':
                d += 1
            elif ruch == 'W':
                p -= 1
            if p < 0 or d < 0 or p > 19 or d > 19:
                pkty = -1
                break
            pkty += int(plansza[d][p])
        if pkty > max_punkty:
            max_punkty = pkty
            max_numer = numer_wiersza
    with open(r'Arkusze/Probna_2019/zadanie4.txt', 'a') as wyniki:
        wyniki.write(f'\n4.2\nGracz numer {max_numer}, ktory uzyskal {max_punkty} punktow.\n')


# 4.3
def nastepujace():
    najwieksza = 1
    for robot in roboty:
        dlugosc = 1
        for n in range(len(robot)-1):
            if (robot[n] == 'W' or robot[n] == 'E') and (robot[n+1] == 'W' or robot[n+1] == 'E'):
                dlugosc += 1
            else:
                if dlugosc > najwieksza:
                    najwieksza = dlugosc
                dlugosc = 1
    numer = 0
    for robot in roboty:
        numer += 1
        if len(robot) < najwieksza:
            continue
        dlugosc = 1
        for n in range(len(robot)-1):
            if (robot[n] == 'W' or robot[n] == 'E') and (robot[n + 1] == 'W' or robot[n + 1] == 'E'):
                dlugosc += 1
            else:
                if dlugosc == najwieksza:
                    with open(r'Arkusze/Probna_2019/zadanie4.txt', 'a') as wyniki:
                        wyniki.write(f'\n4.3\n{numer}\n')
                dlugosc = 1
    with open(r'Arkusze/Probna_2019/zadanie4.txt', 'a') as wyniki:
        wyniki.write(f'Liczba takich ruchow: {najwieksza}\n')


dyskwalifikacja()
punkty()
nastepujace()
