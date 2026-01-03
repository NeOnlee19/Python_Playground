name = input("Jak masz na imię? ")
print("Witaj", name + "!")

answer = input("Stoisz na drodze, zdecyduj czy chcesz iść w lewo czy w prawo. ").lower()
if answer == "lewo":
    answer = input("Dotarłaś do jeziora, możesz je obejść lub przepłynąć. Wpisz 1 lub 2 ")
    if answer == "1":
        print("Przejście jeziora zajęło zbyt dużo czasu, umierasz z wycieńczenia. Przegrywasz")
    elif answer == "2":
        print("Zostałaś zjedzona przez aligatora. Przegrywasz")
    else:
        print("Niepoprawna opcja. Przegrywasz")

elif answer == "prawo":
    answer = input("Dotarłaś do bardzo zniszczonego mostu, zdecyduj czy chcesz przez niego przejść czy zawrócić. Wpisz 1 lub 2 ")
    if answer == "1":
        answer = input("Przeszłaś przez most, na drugim końcu spotykasz obcą osobę. Czy chcesz z nią porozmawiać? Wpisz tak lub nie ")
        if answer == "tak":
            print("Otrzymujesz od nieznajomego złoto. Wygrywasz")
        elif answer == "nie":
            print("Postanawiasz zignorować nieznajomego. Przegrywasz")
        else:
            print("Niepoprawna opcja. Przegrywasz")
    elif answer == "2":
        print("Zawróciłaś z powrotem. Przegrywasz")
    else:
        print("Niepoprawna opcja. Przegrywasz")
else:
    print("Niepoprawna opcja. Przegrywasz")