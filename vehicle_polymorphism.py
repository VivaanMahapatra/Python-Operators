class BMW:
    fuel_type = "Petrol"
    max_speed = 250

    def display(self):
        print("BMW")
        print("Fuel Type:", self.fuel_type)
        print("Max Speed:", self.max_speed, "km/h")


class Ferrari:
    fuel_type = "Petrol"
    max_speed = 340

    def display(self):
        print("Ferrari")
        print("Fuel Type:", self.fuel_type)
        print("Max Speed:", self.max_speed, "km/h")


for vehicle in (BMW(), Ferrari()):
    vehicle.display()
    print()