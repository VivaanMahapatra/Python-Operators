class BMW:
    def speed(self):
        print("BMW runs at 250 km/h")

    def fuel(self):
        print("BMW uses petrol")

class Ferrari:
    def speed(self):
        print("Ferrari runs at 340 km/h")

    def fuel(self):
        print("Ferrari uses petrol")

for car in (BMW(), Ferrari()):
    car.speed()
    car.fuel()
    print()