import random

play = input("Do you want to play? (y/n) ")
if play.lower() == "y":
    print("Starting the game.........")
    guesses = 0
    random_num = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    while guess != random_num:
        if guess < random_num:
            print("To lowww!Try again")
        elif guess > random_num:
            print("To highhh!Try again")
        elif guess > 100 or guess < 1:
            print("Pls enter a number from 1 to 100")
        guess = int(input("Guess a number between 1 and 100: "))
        guesses +=1
    print(f"Congratulations! You guessed the number {random_num} in {guesses} guesses.")
else:
    print("Goodbye!")
    exit()