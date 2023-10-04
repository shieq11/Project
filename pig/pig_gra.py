# Gra polega na rzucie kostką i sumowaniu wyników.
# Sam decydujesz ile razy dokonuje sie rzut
# Jeśli w którymś rzucie trafisz 1 wtedy koniec gry.
# Wynik wcześniejszych rzutów się zeruje
# Jeśli podczas rzutów nie wylosuje się liczba 1 suma dodaje się do totalnej liczby
# Gracze określają ile trzeba uzyskać pkt aby wygrac np powyeżej 50
import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
while True:
    player =  input("Enter the number of player (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2<= player <=4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:
    for player_idx in range(player):
        print("\nPlayer", player_idx +1, "turn has started")
        print("Your total score is:", player_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
             break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your score is:", current_score)

        player_score[player_idx] += current_score
        print("You total score is:", player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("Player number", winning_idx +1, "is the winner witch score of: ", max_score)