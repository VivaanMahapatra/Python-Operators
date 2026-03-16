from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\n the current date and time is", now)
print("\nDate components", today.year, today.month, today.day)