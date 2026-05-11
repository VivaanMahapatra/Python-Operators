import random
import time
guessesTaken = 0
number = random.randint(1, 100)

def intro():
    print("May I ask you for your name?")
    

    global name
    
    name = input("Enter your name : ")  
    
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")

    if(number % 2 == 0):
        x = 'even'
    else:
        x = 'odd'

    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!")
def pick():
    guessesTaken=0
    while guessesTaken<6:
          guessesTaken  = guessesTaken+1
          guess = int(input("Enter a number between 1 and 100 : "))
          if number>guess:
                print(guess,", is less than the number")
          elif number<guess:
                print(guess,", is more than the number")
          elif guess>100 or guess<1:
                print("Invalid guess, try guessing between 1 and 100")
          elif guess==number:
                print("You Guessed The NUMBER!!!")
                break
print("The number was : ",number)
play_again = "y"
while play_again=="y":
     intro()
     pick()
     print("Do you want to play again : ")
     play_again=input()


        

