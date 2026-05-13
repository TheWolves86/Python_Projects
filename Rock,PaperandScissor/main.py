import random
play = input("Do you want to play Rock,Paper and Scissor? (yes/no) ")
def play_game():
    userInput = input("Enter your choice (rock/paper/scissor): ")
    dict1 = {
        1: "rock",
        2: "paper",
        3: "scissor"
    }
    if userInput == "rock":
        userchoice = 1
    elif userInput == "paper":
        userchoice = 2
    elif userInput == "scissor":
        userchoice = 3
    else:
        print("Invalid input. Please choose rock, paper, or scissor.")
    compchoice = random.randint(1, 3)
    if userchoice == compchoice:
        print("It's a tie!")
    elif (userchoice - compchoice) == 1 or (userchoice - compchoice) == -2:
        print(f"You win!Your choice: {dict1[userchoice]}, Computer's choice: {dict1[compchoice]}")
    else:
        print(f"Computer won! Your choice: {dict1[userchoice]}, Computer's choice: {dict1[compchoice]}")
if play.lower() == "yes":
    play_game()
    while True:
        wannaplay = input("Do you want to play again? (yes/no) ")
        if wannaplay.lower() == "yes":
            play_game()
        else:
            print("Byeee")
            break
            exit()
else:
    print("Byeee")
    exit()