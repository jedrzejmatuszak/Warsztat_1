print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach")
min, max = 0, 1000
zgadlem = False
while not zgadlem:
    guess = int((max - min) / 2) + min
    print("Zgaduję: {}".format(guess))
    k = input('Zgadłem? Wybierz nr: 1. Tak, 2. Za dużo, 3. Za mało: ')
    if k == "2":
        max = guess
    elif k == "3":
        min = guess
    elif k == "1":
        print("Wygrałem!")
        zgadlem = True
    else:
        print('NIE OSZUKUJ')

