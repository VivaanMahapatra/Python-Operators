a = 10
b = 5
c = -15

if a>0 and b>0:
    print("Both a and b are greater than 0")
elif a>0 and c>0:
    print("Both a anc c are greater than 0")
elif b>0 and c>0:
    print("Both b anc c are greater than 0")
elif a>0 or b>0:
    print("Either a or b is positive")
elif (a>0 or b>0) or c>0:
    print("Either of the numbers are positive")
elif (a<0 or b<0) or c<0:
    print("Either of the numbers are negative")
else:
    print("All three numbers are negative")
