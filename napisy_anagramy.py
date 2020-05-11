import time

start = time.time()

with open(r'dane/68/dane_napisy.txt') as dane:
    napisy = [__.rstrip().split(' ') for __ in dane.readlines()]


"""
68.1.
Napis nazywamy jednolitym, jeżeli wszystkie jego litery są takie same. Przykładem takiego
napisu jest AAAA. Podaj liczbę wierszy zawierających parę napisów jednolitych, które są
wzajemnie swoimi anagramami. """


def jednolite():
    ile = 0
    for napis in napisy:
        if napis[0] != napis[1]:
            continue
        ile += 1
    with open(r'wyniki/68/wyniki_anagramy.txt', 'w') as wyniki:
        wyniki.write(f'68.1\n{ile}\n')


"""
68.2.
Podaj liczbę wierszy, które zawierają napisy będące wzajemnie swoimi anagramami. """


def anagramy():
    ile = 0
    lista = []
    for napis in napisy:
        lista.append(''.join(sorted(napis[0])))
        lista.append(''.join(sorted(napis[1])))
        if sorted(list(napis[0])) != sorted(list(napis[1])):
            continue
        ile += 1
    with open(r'wyniki/68/wyniki_anagramy.txt', 'a') as wyniki:
        wyniki.write(f'\n68.2\n{ile}\n')

    """
    68.3.
    Podaj największą liczbę k taką, że w pliku znajduje się k napisów, z których każde dwa są
    wzajemnie swoimi anagramami. """
    lista.sort()
    dlugosc = 1
    najwiecej = 0
    for n in range(len(lista)-1):
        if lista[n] == lista[n+1]:
            dlugosc += 1
        else:
            if dlugosc > najwiecej:
                najwiecej = dlugosc
            dlugosc = 1
    with open(r'wyniki/68/wyniki_anagramy.txt', 'a') as wyniki:
        wyniki.write(f'\n68.3\n{najwiecej}\n')


jednolite()
anagramy()

print('--- %s seconds ---' % (time.time() - start))
