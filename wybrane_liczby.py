with open(r'Arkusze/Czerwiec_2019/liczby.txt') as dane:
    liczby = [int(_.rstrip()) for _ in dane.readlines()]

with open(r'Arkusze/Czerwiec_2019/pierwsze.txt') as dane:
    pierwsze = [int(_.rstrip()) for _ in dane.readlines()]

with open(r'Arkusze/Czerwiec_2019/wyniki4.txt', 'w') as wyn:
    wyn.write('')


# 4.1
def pierw():
    with open(r'Arkusze/Czerwiec_2019/wyniki4.txt', 'a') as wyniki:
        wyniki.write('4.1\n')
        for n in liczby:
            if n < 100 or n > 5000:
                continue
            if n in pierwsze:
                wyniki.write(f'{n}, ')


# 4.2
def odwrotne():
    with open(r'Arkusze/Czerwiec_2019/wyniki4.txt', 'a') as wyniki:
        wyniki.write('\n\n4.2\n')
        for n in pierwsze:
            n = int(str(n)[::-1])
            pierwsza = True
            for s in range(2, n//2+1):
                if n % s == 0:
                    pierwsza = False
                    break
            if pierwsza:
                wyniki.write(f'{str(n)[::-1]}, ')


# 4.3
def wagi():
    ile = 0
    for liczba in pierwsze:
        lista = list(str(liczba))
        while len(lista) > 1:
            suma = 0
            for numer in lista:
                suma += int(numer)
            lista = list(str(suma))
        if suma == 1:
            ile += 1
    with open(r'Arkusze/Czerwiec_2019/wyniki4.txt', 'a') as wyniki:
        wyniki.write(f'\n\n4.3\n{ile}')


pierw()
odwrotne()
wagi()
