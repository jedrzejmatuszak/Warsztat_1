from random import randint
from time import sleep

print('Losowanie liczby...')
sleep(2)
print('Lczba została wylosowana. Zgaduj :)', end="\n")
wylosowana_liczba = randint(1, 100)
print(wylosowana_liczba)

zgadywana_wartosc = False
while not zgadywana_wartosc:
    try:
        liczba = input('Zgadnij liczbę: ')
        liczba = int(liczba)
        # poprawna_wartosc = True
        if liczba > wylosowana_liczba:
            print('Za dużo!')
        elif liczba < wylosowana_liczba:
            print('Za mało!')
        else:
            print('Zgadłeś!')
            # break
            zgadywana_wartosc = True
    except ValueError:
        print('To nie jest liczba')

# print('Liczba {} jest poprawna'.format(liczba))
