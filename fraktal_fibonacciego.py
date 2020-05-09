import time

start = time.time()


"""
67.1.
Podaj wartości F10, F20, F30, F40. Zapisz każdą z liczb w osobnym wierszu. """


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


l_fib = []


def make_list():
    for n in range(1, 41):
        l_fib.append(fib(n))


def wartosci():
    make_list()
    with open(r'wyniki/67/wyniki.txt', 'w') as wyniki:
        wyniki.write(f'67.1\n{l_fib[9]}\n{l_fib[19]}\n{l_fib[29]}\n{l_fib[39]}\n')


"""
67.2.
Znajdź wszystkie liczby pierwsze wśród liczb F1, F2, … , F40. Zapisz każdą z liczb w osobnym
wierszu. """


def pierwsza(n):
    return all(n % i for i in range(2, n))


def pierwsze():
    with open(r'wyniki/67/wyniki.txt', 'a') as wyniki:
        wyniki.write('\n67.2\n')
    for n in range(2, 40):
        if pierwsza(l_fib[n]):
            with open(r'wyniki/67/wyniki.txt', 'a') as wyniki:
                wyniki.write(f'{l_fib[n]}\n')


"""
67.3.
Dla pierwszych 40 liczb Fibonacciego utwórz binarny fraktal Fibonacciego:
• Wypisz reprezentację binarną wszystkich liczb Fibonacciego od F1 do F40.
• Wyrównaj długości reprezentacji binarnych wszystkich liczb Fibonacciego od F1 do
F40 i na ich podstawie sporządź obraz binarnego fraktala Fibonacciego. """


def binarny():
    with open(r'wyniki/67/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n67.3\n')
    for n in range(1, 40):
        with open(r'wyniki/67/wyniki.txt', 'a') as wyniki:
            wyniki.write(f'{bin(l_fib[n])[2:]}\n')
        binfib = list(bin(l_fib[n])[2:])
        if len(binfib) < 27:
            for __ in range(27 - len(binfib)):
                binfib.insert(0, '0')
        """print(''.join(n for n in binfib))"""


"""
67.4.
Podaj w zapisie binarnym wyrazy ciągu Fibonacciego z zakresu od F1 do F40, które w tym
zapisie mają dokładnie 6 jedynek. """


def jedynki():
    with open(r'wyniki/67/wyniki.txt', 'a') as wyniki:
        wyniki.write(f'\n67.4\n')
    for n in range(1, 40):
        if str(bin(l_fib[n]))[2:].count('1') == 6:
            with open(r'wyniki/67/wyniki.txt', 'a') as wyniki:
                wyniki.write(f'{bin(l_fib[n])[2:]}\n')


wartosci()
pierwsze()
binarny()
jedynki()

print('--- %s seconds ---' % (time.time() - start))
