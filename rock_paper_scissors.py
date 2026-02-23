import random

while True:
    user_action = input("Chose from the following : ('paper', 'rock', 'scissors') : ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"You chose {user_action} and computer chose {computer_action}.\n")

    if user_action==computer_action:
        print(f"Both of you have chosen {user_action} it is a tie.\n")
    elif user_action=="paper":
         if computer_action=="rock":
              print("Paper covers rock you win!")
         else:
              print("Scissor cuts paper you lose!")
    elif user_action=="rock":
         if computer_action=="paper":
              print("Paper covers rock you lose!")
         else: 
              print("Rock smashes the scissors you win!")
    elif user_action=="scissors":
         if computer_action=="paper":
              print("Scissors cut paper you win!")
         else:
              print("Rock smashes the scissors you lose!")

    play_again = str(input("Do you want to play again? (y/n) : "))
    if play_again!="y":
         break