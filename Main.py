#Import
import random

#Variables
options= ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper Scissors! Keep playing until tired, and enter 'X' to quit.")

#Score
user_score= 0
computer_score= 0

#Continuing game
game= True

while game is True:
    user_input = input("Make a choice from the options of rock, paper and scissors: ")

    if user_input == "X":
        game= False
        break

    while user_input not in options:
        print("Wrong choice, try again")
        user_input = input("Make a choice from the options of rock, paper and scissors: ")

    # Chooses random choice
    comp_option = random.choice(options)

    # Visualizes and prints both players pick
    print(f"Player: {user_input}")
    print(f"Computer: {comp_option}")

    if comp_option == user_input:
        print("It's a tie!")
    elif comp_option == "rock" and user_input == "paper":
        print("You win!")
        user_score+=1
    elif comp_option == "paper" and user_input == "scissors":
        print("You win!")
        user_score+=1
    elif comp_option == "scissors" and user_input == "rock":
        print("You win!")
        user_score+=1
    else:
        print("You lose!")
        computer_score+=1

print("Final Score:")
print(f"Computer Score: {computer_score}")
print(f"Player Score: {user_score}")