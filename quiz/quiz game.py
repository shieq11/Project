# Program polega na zadawaniu uzytkownikowi pytań
# Za każdą poprawną odp. użytkownik otrzymuje 1 pkt
# Na końcu wyświetlana zostaje liczba zdobytych punktów

print("Welcome in my quiz ")

playing = input("CDo you want to play? ")
score = 0

if playing.lower() != "yes":
    print("Ok maybe next time")
    quit()
print("Okay Let's play")

answer = input("What does CPU stand for? " )

if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? " )

if answer.lower() == "graphics prosessing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? " )

if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? " )

if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " question correct!" )