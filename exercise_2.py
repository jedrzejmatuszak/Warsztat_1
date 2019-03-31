# # czy wprowadzony ciąg znaków jest poprawną liczbą,
# # czy użytkownik nie wpisał tej liczby już poprzednio,
# # czy liczba należy do zakresu 1-49,
# liczby_uzytkownika = []
#
# while len(liczby_uzytkownika) <= 6:
#     try:
#         liczba = int(input("Podaj liczbę: "))
#     except ValueError:
#         print("Takich rzeczy nie da się wylosować w lotto!")
#         continue
#
#     if liczba in liczby_uzytkownika:
#         print("Hej wylosowałeś już tą liczbę. Powinienś czegoś nowego!")
#         continue
#
#     if liczba > 49 or liczba < 1:
#         print("Takiego lotto jeszcze nie było!")
#         continue
#
#     liczby_uzytkownika.append(liczba)
#
# print(liczby_uzytkownika)
#
#lotto

from random import randint

slownik_spr={
    3: 'trojke',
    4: 'czworke',
    5: 'piatke',
    6: 'szostke'
}

print('Podaj 6 liczb od 1 do 49, które obstawiasz:')
liczby = []
while len(liczby) < 6:
    try:
        liczba = int(input("Podaj liczbe: "))
        if liczba in liczby:
            print('Liczba została już skreślona. Podaj jeszcze raz.')
            continue

        if liczba > 49 or liczba < 1:
            print('Liczba poza zakresem :(')
            continue

        liczby.append(liczba)
    except ValueError:
        print('To nie jest liczba!')

liczby = sorted(liczby)
print("Twój kupon wygląda tak: {}".format(liczby))

wylosowane_liczby = []
for x in range(6):
    los = randint(1, 49)
    if los in wylosowane_liczby:
        x =- 1
    wylosowane_liczby.append(los)
print("Wylosowano następujące liczby: {}".format(wylosowane_liczby))
spr = 0

for x in liczby:
    if x in wylosowane_liczby:
        spr += 1

if spr < 3:
    print('Niestety, nic nie wygrałeś')
else:
    print('Brawo, trafiłeś {}'.format(slownik_spr.get(spr)))