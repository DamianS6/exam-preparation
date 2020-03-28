liczby = []
with open(r"dane/59/liczby.txt") as dane:
    for __ in dane.readlines():
        liczby.append(int(__.rstrip()))


# 58.1
def rozne_czynniki(l):
    czynnik = 3
    ile_czynnikow = 0
    if l % 2 == 0:
        return False
    while l > 1:
        if l % czynnik == 0:
            ile_czynnikow += 1
            while l % czynnik == 0:
                l //= czynnik
        czynnik += 2
        if ile_czynnikow > 3:
            return False
    if ile_czynnikow == 3:
        return True
    if ile_czynnikow < 3:
        return False


def licz():
    ile = 0
    for l in liczby:
        if rozne_czynniki(l):
            ile += 1
            print(ile)
    return ile


licz()

"""licz = 0
for l in liczby:
    if len(dziel(l)) >= 3:
        print(l, dziel(l))
        licz += 1
return licz"""

# 58.2
def palindromy():
    palindrom = 0
    for l in liczby:
        liczba = str(l + int(str(l)[::-1]))
        if liczba == liczba[::-1]:
            palindrom += 1
    return palindrom


with open(r"wyniki/59/wyniki_liczby.txt", 'w') as wyniki:
    wyniki.write(f"58.1\n{rozne_czynniki()}\n")
    wyniki.write(f"58.2\n{palindromy()}\n")

# 58.3
def licz_moc():
    mini, maxi = liczby[0], liczby[0]
    liczby_mocy = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for l in liczby:
        liczby_mocy[moc(l, 0)] += 1
        if moc(l, 0) == 1:
            if maxi < l:
                maxi = l
            if mini > l:
                mini = l

    with open(r"wyniki/59/wyniki_liczby.txt", 'a') as wyniki:
        wyniki.write(f"58.3\nLiczby o mocy 1: {liczby_mocy[1]}\nLiczby o mocy 2: {liczby_mocy[2]}\n"
                     f"Liczby o mocy 3: {liczby_mocy[3]}\nLiczby o mocy 4: {liczby_mocy[4]}\n"
                     f"Liczby o mocy 5: {liczby_mocy[5]}\nLiczby o mocy 6: {liczby_mocy[6]}\n"
                     f"Liczby o mocy 7: {liczby_mocy[7]}\nLiczby o mocy 8: {liczby_mocy[8]}\n"
                     f"Minimalna liczba o mocy równej 1: {mini}\n"
                     f"Maksymalna liczba o mocy równej 1: {maxi}\n")


def moc(num, k):
    w = 1
    if len(str(num)) == 1:
        return k
    for n in list(str(num)):
        w *= int(n)
    k += 1
    return moc(w, k)


licz_moc()
