play = input("Do you want to start a adventure? (yes/no) ")
if play.lower() == "yes":
    print("You are in a forest which is covered by many trees. There are only 2 options which are left and right. Which way do you wanna go?")
    choice1 = input("(left/right) ")
    if choice1 == "left":
        print("Now you walk and walk and then you dont see a way. There is only a one river. Would you swim or rest")
        choice2 = input("(swim/rest)")
        if choice2 == "swim":
            print("Congrats! You made it out of the forest")
            exit()
        elif choice2 == "rest":
            print("You were resting peacefully but suddenly a Bear came and attacked you and you died.")
            print("--------------------------------------------------------")
            print("Game over!")
            print("--------------------------------------------------------")
            exit()
        else:
            print("Invalid choice. Please choose 'swim' or 'rest'.")
    elif choice1 == "right":
        print("You chose to go right. You find a hidden path that leads to a treasure!")
        exit()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
else:
    print("Byeeee!")
    exit()