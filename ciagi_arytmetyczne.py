import time


start_time = time.time()
with open(r'dane/61/ciagi.txt') as dane:
    ciagi = []
    n = 0
    for ciag in dane.readlines():
        if len(ciag) <= 5:
            ciagi.append([int(ciag.rstrip())])
        else:
            for sign in ciag.rstrip().split(' '):
                ciagi[n].append(int(sign))
            n += 1

with open(r'dane/61/bledne.txt') as dane:
    bledne = []
    n = 0
    for ciag in dane.readlines():
        if len(ciag) <= 5:
            bledne.append([int(ciag.rstrip())])
        else:
            for sign in ciag.rstrip().split(sep=' '):
                bledne[n].append(int(sign))
            n += 1

"""
61.1
Podaj, ile spośród podanych w pliku ciagi.txt ciągów jest ciągami arytmetycznymi.
Znajdź wśród nich ciąg o największej różnicy i oblicz jego różnicę. Liczbę ciągów arytmetycznych
oraz największą różnicę zapisz w pliku wynik1.txt. """


def sprawdzanie():
    ile = 0
    najw_roznica = ciagi[0][2] - ciagi[0][1]
    for ciag in ciagi:
        arytmetyczny = True
        roznica = ciag[2] - ciag[1]
        if roznica <= 0:
            continue
        for num in range(1, len(ciag)-1):
            if ciag[num] + roznica != ciag[num+1]:
                arytmetyczny = False
                break
        if arytmetyczny:
            ile += 1
            if roznica > najw_roznica:
                najw_roznica = roznica
    with open(r'wyniki/61/wynik1.txt', 'w') as wyniki:
        wyniki.write(f'61.1\n'
                     f'Liczba ciagow arytmetycznych: {ile}.\n'
                     f'Najwieksza roznica: {najw_roznica}.')


"""
61.2
Dla każdego podanego ciągu znajdź — jeśli istnieje — największą występującą w nim liczbę,
która jest pełnym sześcianem jakiejś liczby naturalnej. """


def szescian():
    lista_szescianow = [__**3 for __ in range(1, 101)]
    szesciany = []
    for ciag in ciagi:
        najw = 0
        for num in ciag[1:]:
            if num in lista_szescianow and num > najw:
                najw = num
        if najw > 0:
            szesciany.append(najw)
    with open(r'wyniki/61/wynik2.txt', 'w') as wyniki:
        wyniki.write(f'61.2\n'
                     f"{' '.join([str(__) for __ in szesciany])}")


"""
61.3
Plik bledne.txt ma identyczną strukturę jak ciagi.txt, ale zawiera tylko 20 ciągów.
Wiadomo jednak, że wszystkie występujące w nim ciągi są ciągami arytmetycznymi z jednym
błędem: jeden z wyrazów w każdym ciągu został zastąpiony przez liczbę naturalną nienależącą
do ciągu. Dla każdego ciągu znajdź i wypisz błędny wyraz. """


def bledy():
    lista_bledow = []
    for ciag in bledne:
        roznica = ciag[2] - ciag[1]
        # Sprawdzenie czy różnica nie jest błędna - wtedy błędnym wyrazem jest wyraz pierwszy lub drugi.
        if ciag[3] - ciag[2] != roznica and ciag[5] - ciag[4] != roznica:
            roznica = ciag[5] - ciag[4]
            if ciag[1] + 2*roznica == ciag[3]:
                lista_bledow.append(ciag[2])
            else:
                lista_bledow.append(ciag[1])
            continue
        for num in range(1, len(ciag) - 1):
            if ciag[num] + roznica != ciag[num + 1]:
                lista_bledow.append(ciag[num+1])
                break
    with open(r'wyniki/61/wynik3.txt', 'w') as wyniki:
        wyniki.write('61.3\n')
        for __ in lista_bledow:
            wyniki.write(str(__) + '\n')


sprawdzanie()
szescian()
bledy()

print("--- %s seconds ---" % (time.time() - start_time))
