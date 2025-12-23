consumed_units = int(input("Please enter the number of units you have consumed : "))
if(consumed_units<50):
    electricity_bill = (consumed_units*2.6+25)
elif consumed_units<=100:
    electricity_bill = (consumed_units*3.25+3.5)
elif(consumed_units<=200):
    electricity_bill = (consumed_units*5.26+3.5)
else:
    electricity_bill = (consumed_units*8.45+7.5)
print("your electricity bill is", electricity_bill)