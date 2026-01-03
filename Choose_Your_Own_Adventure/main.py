name = input("Jak masz na imię? ")
print("Witaj", name + "!")

answer = input("Stoisz na drodze, zdecyduj czy chcesz iść w lewo czy w prawo. ").lower()
if answer == "lewo":
    answer = input("Dotarłaś do jeziora, możesz je obejść lub przepłynąć. Wpisz 1 lub 2")
    if answer == "1":
        print("Przejście jeziora zajęło zbyt dużo czasu, umierasz z wycieńczenia. Przegrywasz")
    elif answer == "2":
        print("Zostałaś zjedzona przez aligatora. Przegrywasz")
    else:
        print("Niepoprawna opcja. Przegrywasz")
elif answer == "prawo":
    print()
else:
    print("Niepoprawna opcja. Przegrywasz")