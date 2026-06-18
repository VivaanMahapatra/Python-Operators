class Vehicle:
    def __init__(self, fare):
        self.fare = fare


class Bus(Vehicle):
    def __init__(self, fare, passengers):
        super().__init__(fare)
        self.passengers = passengers

    def total_fare(self):
        return self.fare * self.passengers

fare_per_person = float(input("Enter fare per passenger: "))
passengers = int(input("Enter number of passengers: "))

bus = Bus(fare_per_person, passengers)

print("Total Fare =", bus.total_fare())