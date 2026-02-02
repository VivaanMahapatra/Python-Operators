def addition(P, Q):
    return (P+Q)
def subtract(P, Q):
    return(P-Q)
def multiplication(P,Q):
    return(P*Q)
def division(P, Q):
    return(P/Q)


num_1 = int(input("Please enter a number : "))
num_2 = int(input("Please enter a number : "))
print("choose whether you want to do addition (A), subtraction (B), multiplication (C), division (D)")
choice = input("Input one of the 4 letters in capitals : ")
if choice == "A":
    print("The addition of the 2 numbers are,", num_1+num_2)
elif choice == "B":
    print("The subtraction of the 2 numbers are,", num_1-num_2)
elif choice == "C":
    print("The multiplication of the 2 numbers are,", num_1*num_2)
elif choice == "D":
    print("The division of the 2 numbers are,", num_1/num_2)
else:
    print("Invalid Input")