class Car:
    def move(self):
        print("Car is driving")

class Boat:
    def move(self):
        print("Boat is sailing")

class Aeroplane:
    def move(self):
        print("Aeroplane is flying")
        
for vehicle in (Car(), Boat(), Aeroplane()):
    vehicle.move()