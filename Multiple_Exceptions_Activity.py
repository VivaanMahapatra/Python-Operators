try:
    num1, num2 = eval(input("Enter 2 numbers, seperated by a comma : "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by 0 is error")
except SyntaxError:
    print("Comma is missing enter numbers seperate by comma")
except:
    print("Wrong Input")
else:
    print("No exceptions")
finally:
    print("This will exectue no matter what")