Max_Lines = 3
Max_Bet = 100
Min_Bet = 1

def deposit():
    while True:
        amount = int(input("Enter the amount you want to deposit: $"))
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            break
    return amount

def get_number_of_lines():
    while True:
        lines = int(input(f"Enter the number of lines to bet on (1-{Max_Lines}): "))
        if lines < 1 or lines > Max_Lines:
            print(f"Number of lines must be between 1 and {Max_Lines}")
        else:
            break
    return lines

def get_bet():
    while True:
        amount = int(input(f"Enter the bet amount (${Min_Bet}-${Max_Bet}): "))
        if amount < Min_Bet or amount > Max_Bet:
            print(f"Bet amount must be between ${Min_Bet} and ${Max_Bet}")
        else:
            break
    return amount

def main():
    print("Welcome to the slot machine!")
    print("---------------------------------")
    balance = deposit()
    print(f"You have a balance of ${balance}")
    print("---------------------------------")
    lines = get_number_of_lines()


main()