# Base class
class Vehicle:
    def start_engine(self):
        print("Starting the vehicle engine")

# Subclass
class Car(Vehicle):
    # Overriding the method from Vehicle
    def start_engine(self):
        print("Starting the car engine with a key")

# Another subclass
class ElectricCar(Vehicle):
    # Overriding the method from Vehicle
    def start_engine(self):
        print("Starting the electric car engine silently")

# Using the classes
vehicle = Vehicle()
vehicle.start_engine()  

car = Car()
car.start_engine()      

tesla = ElectricCar()
tesla.start_engine()    
