import random

user_wins = 0
computer_wins = 0
options = ['papier', 'kamień', 'nożyce']

while True:
    user_input = input("Wybierz Papier/Kamień/Nożyce lub Q, żeby wyjść ").lower()
    if user_input == "q":
        print("Zakończono program")
        break
    if user_input not in options:
        continue

    r = random.randint(0, 2)
    # papier: 0, kamień: 1, nożyce: 2
    computer_pick = options[r]
    print("Komputer wybrał", computer_pick)

    if user_input == "papier" and computer_pick == "kamień":
        print("Wygrałaś!")
        user_wins += 1

    elif user_input == "kamień" and computer_pick == "nożyce":
        print("Wygrałaś!")
        user_wins += 1

    elif user_input == "nożyce" and computer_pick == "papier":
        print("Wygrałaś!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Remis")

    else:
        print("Przegrałaś!")
        computer_wins += 1


print("Wygrałaś", user_wins, "razy")
print("Komputer wygrał", computer_wins, "razy")