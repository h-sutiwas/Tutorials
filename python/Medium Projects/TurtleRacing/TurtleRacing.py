def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of turtles to race (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print(f"Input is not numeric... Try Again!")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number should be between 2 - 10... Try Again!")
    
    return racers

def main():
    racers = get_number_of_racers()
    print(racers)

main()