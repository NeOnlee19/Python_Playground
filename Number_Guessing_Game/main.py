import random

top_of_range = input("Wpisz liczbę: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Następnym razem podaj liczbę większą od 0")
        quit()
else:
    print("Następnym razem podaj liczbę")
    quit()

r = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Zgadnij liczbę: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Następnym razem podaj liczbę")
        continue

    if user_guess == r:
        print("Zgadłaś!")
        break
    elif user_guess > r:
        print("Za dużo!")
    else:
        print("Za mało!")

print("Zgadłaś po", guesses, "próbach")
