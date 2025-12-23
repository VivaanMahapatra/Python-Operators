medical_cause = input("Do you have any medical cause? y/n : ")
attendance = int(input("Input the attendance of the student in percentage : "))
if (medical_cause=="y"):
   print("You are allowed to attend the exam")
else :
  if (attendance>75):
        print("You are allowed to attend the exam")
  else:
        print("You aren't allowed to attend the exam")
         