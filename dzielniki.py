import math


with open(r"dane/60/liczby.txt") as dane:
    liczby = [int(__.rstrip()) for __ in dane.readlines()]

"""
60.1 Policz, ile jest w pliku wejściowym liczb mniejszych niż 1000, oraz podaj dwie takie liczby,
które pojawiają się w pliku jako ostatnie (możesz założyć, że będą co najmniej dwie)."""


def ile_mniejszych():
    mniejsze = [l for l in liczby if l < 1000]
    with open(r"wyniki/60/wyniki.txt", 'w') as wyniki:
        wyniki.write(f'60.1\nLiczb mniejszych niz 1000 jest {len(mniejsze)}. '
                     f'Dwie ktore w pliku pojawiaja sie jako ostatnie, to {mniejsze[-2]} i {mniejsze[-1]}.\n60.2\n')


"""
60.2 Wśród liczb występujących w pliku wejściowym znajdź te, które mają dokładnie 18 dzielników
naturalnych (wliczając w nie 1 i samą liczbę). Dla każdej znalezionej liczby wypisz,
oprócz jej wartości, listę wszystkich jej dzielników, posortowaną rosnąco."""


def osiemnascie_dzielnikow():
    for l in liczby:
        dzielniki = [1]
        n = 2
        while n <= l//2 + 1:
            if l % n == 0:
                dzielniki.append(n)
            n += 1
        if len(dzielniki) == 17:
            dzielniki.append(l)
            with open(r"wyniki/60/wyniki.txt", 'a') as wyniki:
                wyniki.write(f'{l}: {dzielniki}\n')


"""
60.3 Znajdź największą liczbę w pliku, która jest względnie pierwsza ze wszystkimi pozostałymi,
czyli taką, która z żadną z pozostałych liczb nie ma wspólnego dzielnika innego niż 1."""


def wzglednie():
    najw = 2
    for l in liczby:
        wzgledna = True
        for n in liczby:
            if l != n and math.gcd(l, n) > 1:
                wzgledna = False
        if wzgledna and l > najw:
            najw = l

    with open(r"wyniki/60/wyniki.txt", 'a') as wyniki:
        wyniki.write(f'60.3\n{najw}')


ile_mniejszych()
osiemnascie_dzielnikow()
wzglednie()
