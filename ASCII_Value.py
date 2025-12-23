ch = input("Enter a character: ")

for i in range(256):
    if chr(i) == ch:
        print("The ASCII value of", ch, "is", i)
        