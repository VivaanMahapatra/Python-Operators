Withdraw_Amount = int(input("Please enter the amount for withdraw : "))

note1 = Withdraw_Amount//100
note2 = (Withdraw_Amount%100)//50
note3 = ((Withdraw_Amount%100)%50)//10

print("You will be using,", note1, "amount of 100 ruppee notes")
print("You will be using,", note2, "amount of 50 ruppee notes")
print("You will be using,", note3, "amount of 10 ruppee notes")