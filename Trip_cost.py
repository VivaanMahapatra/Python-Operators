def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "Bangalore"==city:
        return 150
    elif "Delhi"==city:
        return 200
    elif "Kolkata"==city:
        return 100
    elif "New York"==city:
        return 2000

def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of the car rental : ", rental_car_cost(5))
print("Cost of the plane ride : ", plane_ride_cost("New York"))
print("Cos of the hotel room : ", hotel_cost(7)) 
print("Total cost of the trip : ",trip_cost("New York",7,500))
print(trip_cost("Delhi",6,500))