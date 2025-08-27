import logging

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input("How much money would you like to deposit? ($)")
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
        lines = input(f"How lines would you want to bet on? (1 - {MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of betting lines must be more than 0....")
        else:
            print("Please enter a number!!!")
        
    return lines

def main():
    amount = deposit()
    lines = get_number_of_lines()
    
    
    # print(f"{amount}, {lines}")
    
main()