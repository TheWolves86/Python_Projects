import random
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

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings


def spin_slot(ROWS, COLUMNS, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(COLUMNS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_result(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


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

def spin(balance):
    print("Welcome to the slot machine!")
    print("---------------------------------")
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
    slots = spin_slot(ROWS, COLUMNS, symbol_count)
    print_slot_result(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}"); 
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
