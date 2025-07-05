import random
from collections import Counter

def startGame():
    playerChooseToPlay = input("Hey there!!! Welcome to the Hangman Game, To play the game type e if not type q: ")
    if playerChooseToPlay.lower() == "q":
        return "Okay, have a nice day !!!"
    elif playerChooseToPlay.lower() == "e":
        
        wordsSeries = """apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"""
        wordsSeries = wordsSeries.split(' ')
        word = random.choice(wordsSeries)
        
        wantToPlay = True
        
        return wantToPlay, word
    else:
        return "Wrong input, please type either e or q !!!!"
    
def gameStructure(wantToPlay: bool, word: str):
    letterGuessed = ""
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    print('Guess the word! HINT: word is a name of a fruit')
    
    for i in word:
        print('_', end=' ')
    print()
    
    try:
        while (chances != 0) and (flag == 0):
            print()
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter')
                continue
            
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif Counter(letterGuessed) == Counter(word):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                    break
                else:
                    print('_', end=' ')
        
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again next time....')
            print('The word was {}'.format(word))
            
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

if __name__ == "__main__":
    wantToPlay, word = startGame()
    gameStructure(wantToPlay, word)