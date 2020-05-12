import time

start = time.time()

with open(r'dane/74/hasla.txt') as dane:
    hasla = [__.rstrip() for __ in dane.readlines()]

liczba = 0
powtorzenia = []
cztery_ascii = 0
bezpieczne = 0

for haslo in hasla:

    """
    74.1.
    Podaj liczbę haseł złożonych jedynie ze znaków numerycznych, tzn. cyfr od 0 do 9. """
    if haslo.isdigit():
        liczba += 1

    """
    74.2.
    Wypisz hasła, które zostały użyte przez co najmniej dwóch różnych użytkowników, tzn. występujące
    w dwóch różnych wierszach. Hasła wypisz (bez powtórzeń) w kolejności leksykograficznej. """
    if hasla.count(haslo) > 1:
        if haslo not in powtorzenia:
            powtorzenia.append(haslo)

    """
    74.3.
    Podaj liczbę użytkowników posiadających hasła, w których występuje fragment złożony
    z czterech kolejnych znaków ASCII (w dowolnej kolejności). """
    for n in range(len(haslo)-3):
        if len(haslo) < 4:
            continue
        if ord(sorted(haslo)[n]) == ord(sorted(haslo)[n+1]) - 1 ==\
                ord(sorted(haslo)[n+2]) - 2 == ord(sorted(haslo)[n+3]) - 3:
            cztery_ascii += 1
            break

    """
    74.4.
    Podaj liczbę haseł, które spełniają jednocześnie poniższe warunki:
    • hasło zawiera co najmniej jeden znak numeryczny, tzn. cyfrę od 0 do 9,
    • hasło zawiera co najmniej jedną małą literę,
    • hasło zawiera co najmniej jedną dużą literę. """
    number, lower, capital = False, False, False
    for char in haslo:
        if char.isdigit():
            number = True
        if char.islower():
            lower = True
        if char.isupper():
            capital = True
    if number and lower and capital:
        bezpieczne += 1

with open(r'wyniki/74/wyniki_hasla.txt', 'w') as wyniki:
    wyniki.write(f'74.1\n{liczba}\n\n74.2\n')
    for haslo in sorted(powtorzenia):
        wyniki.write(f'{haslo}\n')
    wyniki.write(f'\n74.3\n{cztery_ascii}\n\n74.4\n{bezpieczne}')

print(f'--- {time.time() - start} seconds ---')
