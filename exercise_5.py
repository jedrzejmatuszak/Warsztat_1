from random import randint


def kostka_do_gry(kod):
    kostki = (3, 4, 6, 8, 10, 12, 20, 100)
    kod = kod.upper()
    if kod[0] == 'D':
        if '+'in kod:
            typ_kostki = kod[kod.index('D') + 1: kod.index('+')]
            modyfikator = kod[kod.index('+'):]
            liczba_rzutow = 1
            print("Pojedynczy rzut kostka {}-sciena. Wynik zmieniamy o {},".format(typ_kostki, modyfikator), end=" ")
        elif '-' in kod:
            typ_kostki = kod[kod.index('D') + 1: kod.index('-')]
            modyfikator = kod[kod.index(('-')):]
            liczba_rzutow = 1
            print("Pojedynczy rzut kostka {}-sciena. Wynik zmieniamy o {}.".format(typ_kostki, modyfikator), end=" ")
        else:
            liczba_rzutow = 1
            typ_kostki = kod[kod.index('D') + 1:]
            modyfikator = 0
            print("Pojedynczy rzut kostka {}-scianną.".format(typ_kostki), end=" ")
    elif '+' in kod:
        liczba_rzutow = kod[:kod.index('D')]
        typ_kostki = kod[kod.index('D') + 1:kod.index('+')]
        modyfikator = kod[kod.index('+'):]
        print("{} rzutow kostka {}-scienna. Wynik zmieniamy o {}.".format(liczba_rzutow, typ_kostki, modyfikator), end=" ")
    elif '-' in kod:
        liczba_rzutow = kod[:kod.index('D')]
        typ_kostki = kod[kod.index('D') + 1:kod.index('-')]
        modyfikator = kod[kod.index('-'):]
        print("{} rzutow kostka {}-scienna. Wynik zmieniamy o {}.".format(liczba_rzutow, typ_kostki, modyfikator), end=" ")
    else:
        liczba_rzutow = kod[:kod.index('D')]
        typ_kostki = kod[kod.index('D') + 1:]
        modyfikator = 0
        print("{} rzutow kostka {}-scienna.".format(liczba_rzutow, typ_kostki), end=" ")

    if int(typ_kostki) not in kostki:
        raise Exception("Nie ma kostki {}-sciennej!".format(typ_kostki))
    value = 0
    for x in range(int(liczba_rzutow)):
        los = randint(1, int(typ_kostki))
        value += los
    return "Wynik rzutu kośćmi to; {}.".format(value + int(modyfikator))


print(kostka_do_gry('D6'))
print(kostka_do_gry('2D3'))
print(kostka_do_gry('500D100'))
print(kostka_do_gry('2D10+10'))
print(kostka_do_gry('3D10-10'))
print(kostka_do_gry('D100+10'))
print(kostka_do_gry('D20-5'))
print(kostka_do_gry('15d40+66'))