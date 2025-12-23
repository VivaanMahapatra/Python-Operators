first_choice = input("Please enter whether you would like to buy a bike or a car : ")
if first_choice=="car":
    second_choice = input("Please enter whether you would like to buy a sedan or a SUV : ")
    if second_choice == "SUV":
        print("You have chosen to buy an SUV")
    else:
        print("You have chosen to buy a sedan")
elif first_choice=="bike":
    second_choice = input("Please enter whether you would like to buy a scooty or a scooter : ")
    if second_choice == "scooter":
       print("You have chosen to buy a scooter")
    else:
        print("You have chosen to buy a scooty")
else:
    print("you would like to buy a", first_choice)
