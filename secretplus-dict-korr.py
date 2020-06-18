import json
import random
import datetime

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read()) # --> wandelt Liste in Zeichenkette um (json=java script object notation) dient der Umwandlung von komplexen Datenstrukturen (zB Listen o. Dictionaries; od Kommunikation zw Programmiersprachen) in Zeichenketten
    print("Top scores: " + str(score_list))

score_list.sort()
print(score_list[:3]) # wählt die linkesten drei Elemente aus ("Gib mir nur die ersten 3 Elemente der Liste aus - 0-1-2)

while True:
    guess = int(input("Guess the secret number between 1 and 30: "))
    attempts += 1

    if guess == secret:
        score_list.append(attempts) # fügt Element rechts an Liste an (Datenstruktur)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list)) # --> wandelt Zeichenkette in Liste um (Gegenstück zu json.loads)

        print("You guessed it - congrats! It was number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Try a smaller number!")
    elif guess < secret:
        print("Try a higher number!")