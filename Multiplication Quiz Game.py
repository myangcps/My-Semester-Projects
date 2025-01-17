#Multiplication Quiz Game

#Initialize
import random
import time

#Functions
#Creates multiplication solving game with difficulty levels, requested number of questions, timer, and score tracker
def multiplication_game():
    score = 5
    print("Welcome to the Multiplication Quiz Game!")
    while True:
        difficulty = input("Please choose a difficulty level. (Easy, Medium, Hard)")
        difficulty = difficulty.lower()
        if difficulty == "easy":
            start = time.time()
            for i in range(5):
                num1 = random.randint(1, 5)
                num2 = random.randint(1, 5)
                question = input("What is " + str(num1) + " multipled by " + str(num2) + " ?" )
                answer = (num1 * num2)
                if int(question) == num1 * num2:
                    print("Good job, your answer is correct!")
                else:
                    score = score - 1
                    print("Sorry, the answer is incorrect.")
        elif difficulty == "medium":
            start = time.time()
            for i in range(5):
                num1 = random.randint(1, 10)
                num2= random.randint(1, 10)
                question = input("What is " + str(num1) + " multipled by " + str(num2) + " ?" )
                answer = (num1 * num2)
                if int(question) == num1 * num2:
                    print("Good job, your answer is correct!")
                else:
                    score = score - 1
                    print("Sorry, the answer is incorrect.")
        elif difficulty == "hard":
            start = time.time()
            for i in range(5):
                num1 = random.randint(1, 15)
                num2 = random.randint(1, 15)
                question = input("What is " + str(num1) + " multipled by " + str(num2) + " ?" )
                answer = (num1 * num2)
                if int(question) == num1 * num2:
                    print("Good job, your answer is correct!")
                else:
                    score = score - 1
                    print("Sorry, the answer is incorrect.")
        print("Congratulations, your score is " + str(score) + " out of 5.")
        end = time.time()
        length = end - start
        print("It took you " + str(length) + " seconds")
        answer = input("Would you like to keep playing (Yes or No)?")
        answer = answer.lower()
        if answer == "yes":
            pass
        if answer == "no":
            print("Thank you for playing the Multiplication Quiz Game!")
            break
#Main
multiplication_game()
