import random
import sys

def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)
    return value

while True:
    players_count = int(input("Enter the number of players (2-4): "))
    if 2 <= players_count <= 4:
        break
    else:
        print("Please enter a number between 2 and 4.")

target_score = 50
player_scores = [0 for i in range(players_count)]

while max(player_scores) < target_score:
    round_had_score = False
    for player_idx in range(players_count):
        print(f"\nPlayer {player_idx+1} turn has justtt started!")
        print(f"Your total score is: {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n) or quit (q)? ")
            if should_roll.lower() == "q":
                print("Game ended by user.")
                sys.exit()
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f"Your score is: {current_score}")

        player_scores[player_idx] += current_score
        print(f"Your total score is: {player_scores[player_idx]}")
        if current_score > 0:
            round_had_score = True
    if not round_had_score:
        print("No one scored this round. Ending game.")
        break

    winning_score = max(player_scores)
    winning_idx = player_scores.index(winning_score)
    print(f"Player number {winning_idx + 1} is the winner with a score of {winning_score}")
