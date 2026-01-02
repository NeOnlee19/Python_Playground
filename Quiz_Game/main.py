print("-----Quiz Game-----")
playing = input("Czy chcesz rozpocząć nową grę? ")
if playing.lower() != "tak":
    quit()

print("Gra rozpoczęta!")
score = 0

answer = input("Co oznacza skrót CPU? ")
if answer.lower() == "central processing unit":
    print("Brawo! To jest poprawna odpowiedź")
    score += 1
else:
    print("Źle!")

answer = input("Co oznacza skrót GPU? ")
if answer.lower() == "graphics processing unit":
    print("Brawo! To jest poprawna odpowiedź")
    score += 1
else:
    print("Źle!")

answer = input("Co oznacza skrót RAM? ")
if answer.lower() == "random access memory":
    print("Brawo! To jest poprawna odpowiedź")
    score += 1
else:
    print("Źle!")

answer = input("Co oznacza skrót PSU? ")
if answer.lower() == "power supply unit":
    print("Brawo! To jest poprawna odpowiedź")
    score += 1
else:
    print("Źle!")

print("Liczba zdobytych punktów: " + str(score) + "/4")
print("Wynik: " + str((score / 4) * 100) + "%")