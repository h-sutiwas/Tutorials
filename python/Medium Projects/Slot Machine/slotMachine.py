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

def main():
    amount = deposit()
    
main()