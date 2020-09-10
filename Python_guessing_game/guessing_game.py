# game that guesses a number

"""
- assign a random number between 1 and 10
- you only get 5 guesses to guess the num
- after the 5 guesses are over then state "win" or "loss"
"""

import random
import PySimpleGUI as gui

number = random.randint(0, 5)
numOfGuesses = 0

gui.theme('Black')

layout = [  [gui.Text('We have assigned a number... now you have to guess it...')], guiText('Some text on Row 1')],
            [gui.MLine(key='-ML2-' + gui.WRITE_ONLY_KEY,  size=(40,8))],
            [gui.Button('Play Again'), gui.Button('Stop')]],

window = gui.Window('Python Guessing Game', layout, finalize = True)

# Note, need to finalize the window above if want to do these prior to calling window.read()
window['-ML1-' + gui.WRITE_ONLY_KEY].print('\n', end='')
window['-ML1-' + gui.WRITE_ONLY_KEY].print(1,2,3,4,text_color='white', background_color='green')
counter = 0

while True:
    event, values = window.read(timeout=100)

while numOfGuesses < 5:

    event, values = window.read(timeout=100)

    guess = int(input("What is your guess: "))

    if guess == number:
        print("YOU GUESSED THE NUMBER CORRECTLY, THE NUMBER WAS " + str(number))

        playAgain = input("WOULD YOU LIKE TO PLAY AGAIN?: ")

        if event == 'Play again':
            counter += 1
            numOfGuesses = 0
            number = random.randint(0, 5)

        if event in (gui.WIN_CLOSED, 'Stop'):
            numOfGuesses = 6

    else:
        print("YOU SUCK, WRONG ANSWER, TRY AGIAN!")
        print(number)

    numOfGuesses = numOfGuesses + 1

window.close()




#game logic ----------------------------------



while numOfGuesses < 5:

    guess = int(input("What is your guess: "))

    if guess == number:
        print("YOU GUESSED THE NUMBER CORRECTLY, THE NUMBER WAS " + str(number))

        playAgain = input("WOULD YOU LIKE TO PLAY AGAIN?: ")

        if playAgain == "yes":
            numOfGuesses = 0
            number = random.randint(0, 5)

        if playAgain == "no":
            numOfGuesses = 6

    else:
        print("YOU SUCK, WRONG ANSWER, TRY AGIAN!")
        print(number)

    numOfGuesses = numOfGuesses + 1

if numOfGuesses == 5:
    print("GAME OVER, WOULD YOU LIKE TO TRY AGIAN?")
