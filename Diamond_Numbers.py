rowSize = int(input("enter the number of rows: "))
if rowSize % 2 == 0:     
    halfDiamRow = rowSize / 2
else:                   
    halfDiamRow = rowSize / 2 + 1
space = halfDiamRow - 1
for i in range(1, halfDiamRow + 1):
    for j in range(1, space + 1):
        print(" ", end="")
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num = num + 1
    print()
space = 1
for i in range(1, halfDiamRow):
    for j in range(1, space + 1):
        print(" ", end="")
    space = space + 1
    num = 1
    for j in range(1, 2 * (halfDiamRow - i)):
        print(num, end="")
        num = num + 1
    print()
