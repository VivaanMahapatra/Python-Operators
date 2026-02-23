import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0-9 and you will have to guess the number one digit at a time \n")
print("The game ends when you guess a number right")

while playing:
    guess = (input("Give me your best guess : "))
    if number==guess:
        print("You WIN!")
        print("The number was indeed", number)
        break  
    else:
        print("Your guess isn't right try again")