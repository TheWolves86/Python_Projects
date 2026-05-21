Max_Lines = 3
Max_Bet = 100
Min_Bet = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def spin(ROWS, COLUMNS, symbol_count):
    pass




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
        amount = int(input(f"Would you like to bet on each line: $"))
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
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You do not have enough balance")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")

main()