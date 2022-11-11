class Vehicle():
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display(self):
        print("Vehicle Type:" + self.type)
        print("Vehicle Year:" + self.year)
        print("Vehicle Make:" + self.make)
        print("Vehicle Model:" + self.model)
        print("Number of Doors:" + self.doors)
        print("Type of Roof:" + self.roof)

type = input("Vehicle Type: ")
year = input("Vehicle Year: ")
make = input("Vehicle Make: ")
model = input("Vehicle Model:")
doors = input("Number of Doors (2 or 4): ")
roof = input("Type of roof (solid or sunroof: ")
new_vehicle = Automobile(type, year, make, model, doors, roof)
new_vehicle.display()