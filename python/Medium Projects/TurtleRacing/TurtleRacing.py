import time
import random
import turtle

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

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
    
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    pass


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

def main():
    racers = get_number_of_racers()

    init_turtle()
    random.shuffle(COLORS)
    
    colors = COLORS[:racers]
    race
    
    racer = turtle.Turtle()
    time.sleep(5)

main()