def systemy():
    with open(r"dane\58\dane_systemy1.txt") as dane:
        stacja1 = [list(__.rstrip().split(' ')) for __ in dane.readlines()]
    with open(r"dane\58\dane_systemy2.txt") as dane:
        stacja2 = [list(__.rstrip().split(' ')) for __ in dane.readlines()]
    with open(r"dane\58\dane_systemy3.txt") as dane:
        stacja3 = [list(__.rstrip().split(' ')) for __ in dane.readlines()]

    measures_len = max(len(stacja1), len(stacja2), len(stacja3))  # W razie gdyby pliki były różnej długości.

    for i in range(measures_len):
        for x in range(2):
            stacja1[i][x] = int(stacja1[i][x])
            stacja2[i][x] = int(stacja2[i][x])
            stacja3[i][x] = int(stacja3[i][x])

    # 58.1 Dla każdej stacji pogodowej podaj najniższą zarejestrowaną temperaturę, a wszystkie wyniki
    # zapisz w systemie binarnym (dwójkowym).
    minim1 = stacja1[0][1]
    for i in stacja1:
        if minim1 > i[1]:
            minim1 = i[1]

    minim2 = stacja1[0][1]
    for i in stacja2:
        if minim2 > i[1]:
            minim2 = i[1]
    minim2 = bin(int(str(minim2), 4))  # Zamiana z czwórkowego na binarny przez dziesiętny.
    minim2 = -1*int(str(minim2)[3:])  # Usunięcie pierwszych dwóch bitów '0b' po znaku liczby.

    minim3 = stacja3[0][1]
    for i in stacja3:
        if minim3 > i[1]:
            minim3 = i[1]
    minim3 = bin(int(str(minim3), 8))  # Jw. dla ósemkowego.
    minim3 = -1 * int(str(minim3)[3:])

    # 58.2 Podaj liczbę pomiarów, w których zarejestrowany stan zegara był niepoprawny jednocześnie
    # we wszystkich stacjach pogodowych.
    error = 0
    for i in range(measures_len):
        if int(str(stacja1[i][0]), 2) % 12 != 0 and int(str(stacja2[i][0]), 4) % 12 != 0 \
                and int(str(stacja3[i][0]), 8) % 12 != 0:  # Sprawdzenie czy liczby w dziesiętnym są podzielne przez 12.
            error += 1

    # 58.3 Dniem rekordowym jest dzień, w którym w co najmniej jednej stacji pogodowej zarejestrowano
    # rekord temperatury. Podaj liczbę dni rekordowych.
    rekord = 1  # Pierwszy pomiar również jest rekordem.
    rekord1, rekord2, rekord3 = stacja1[0][1], stacja2[0][1], stacja3[0][1]
    for i in range(measures_len):
        rec = False
        if stacja1[i][1] > rekord1:
            rec = True
            rekord1 = stacja1[i][1]
        if stacja2[i][1] > rekord2:
            rec = True
            rekord2 = stacja2[i][1]
        if stacja3[i][1] > rekord3:
            rec = True
            rekord3 = stacja3[i][1]
        if rec:
            rekord += 1

    # 58.4 Podaj największy skok temperatury w stacji pogodowej S1. Wynik podaj w systemie dziesiętnym.
    skok = 0
    for i in range(len(stacja1)):
        for j in range(len(stacja1)):
            roznica = (int(str(stacja1[i][1]), 2) - int(str(stacja1[j][1]), 2))**2
            if abs(i-j) == 0:
                continue
            iloraz = roznica/abs(i-j)
            if iloraz != int(iloraz):
                iloraz += 1
            if iloraz > skok:
                skok = int(iloraz)

    with open(r"wyniki\58\wyniki_systemy.txt", "w") as wyniki:
        wyniki.write(f'58.1\nStacja S1: {minim1}\nStacja S2: {minim2}\nStacja S3: {minim3}\n')
        wyniki.write(f'58.2\n{error}\n')
        wyniki.write(f'58.3\n{rekord}\n')
        wyniki.write(f'58.4\n{skok}')


systemy()
