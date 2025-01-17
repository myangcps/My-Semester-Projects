#Rock Paper Scissors

#Initialize
import random
#Functions
#Step 1: Obtain the player's move

print("Welcome to the game of rock, paper, scissors.")
print("What is your move?")
def game():
    wins = 0
    losses = 0
    while True:
        player = input("rock, paper, scissors, Go: ") #String
        player = player.lower()
    #Step 2: Generate the computer's move

        computer = random.randint(1, 3)
        if computer == 1:
            computer = "rock"
            print("The computer's move is rock.")
        elif computer == 2:
            computer = "paper"
            print("The computer's move is paper.")
        else:
            print("The computer's move is scissors")

    #Step 3: The outcome

        if player == "rock" and computer == "rock":
            print("Tie")
        elif player == "paper" and computer == "paper":
            print("Tie")
        elif player == "scissors" and computer == "scissors":
            print("Tie")
        elif player == "rock" and computer == "paper":
            print("Computer wins")
            losses = losses + 1
        elif player == "rock" and computer == "scissors":
            print("Player wins")
            wins = wins + 1
        elif player == "paper" and computer == "rock":
            print("Player wins")
            wins = wins + 1
        elif player == "paper" and computer == "scissors":
            print("Computer wins")
            losses = losses + 1
        elif player == "scissors" and computer == "rock":
            print("Computer wins")
            losses = losses + 1
        elif player == "scissors" and computer == "paper":
            print("Player wins")
            wins = wins + 1

        print(str("You have " + str(wins) + " wins and " + str(losses) + " losses"))
    #Step 4: Loop the game until player wants to quit

        print("Would you like to keep playing?")
        player = input("Yes or No?")
        player = player.lower()
        if player == "yes":
            pass
        if player == "no":
            break

#Step 5: Keep track of the player's wins and losses
#Included in Step #3
#Main
game()
