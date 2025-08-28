import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 6,
    "C": 8,
    "D": 10
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
                
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

# Example Of Columns
# [A, B, C]
# [B, B, B]
# [C, C, C]

# Loop Explanation

## Step 1 
# columns[0] = [A, B, C] with len of this equal to 3
# row value start with 0

## Step 2
# Then we execute another loop inside with
# enumerate(columns) => i, column start with 0, [A, B, C]

## Step 3
# Check if i is not equal to the last column (in this case it's if i is not 2)
# then print the column[row] that end with "|"
# column[row] = A


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()


def deposit():
    while True:
        amount = input("How much money would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount of deposit must be more than 0....")
        else:
            print("Please enter a number!!!")
        
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"How lines would you want to bet on? (1 - {MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of betting lines must be more than 0....")
        else:
            print("Please enter a number!!!")
        
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number!!!")
        
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. \nTotal bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    # print(f"{amount}, {lines}")
    
main()