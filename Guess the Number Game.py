#Number Guesser

#Initialize
import random

#Functions
#Generates random number and checks if user is correct or incorrect, while also counting the number of lives.
def guessNumber():
    number=int(random.randint(1,10))
    while number < 10:
        firstGuess=int(input("Guess the number (1-10) 3 lives left"))
        if firstGuess == number:
            print("Good job, you guessed the number")
        elif firstGuess != number and firstGuess < number:
            print("Incorrect, your input is too low, please try again")
        elif firstGuess != number and firstGuess > number:
            print("Incorrect, your input is too high, please try again")
        break
    secondGuess=int(input("Guess the number (1-10) 2 lives left"))
    if secondGuess == number:
        print("Good job, you guessed the number")
    elif secondGuess != number and secondGuess < number:
        print("Incorrect, your input is too low, please try again")
    elif secondGuess != number and secondGuess > number:
        print("Incorrect, your input is too high, please try again")
    thirdGuess=int(input("Guess the number (1-10) 1 lives left"))
    if thirdGuess == number:
        print("Good job, you guessed the number")
    else:
        print("YOU LOST and the number is " + str(number))
#Main
guessNumber()
