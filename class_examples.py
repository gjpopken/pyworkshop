# class_example.py

class Vehicle:

    # number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

class Car(Vehicle):
    number_of_wheels = 4

class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)

daily_driver = Car("Subaru", "Crosstrek")
print(f"I drive a {daily_driver.make} {daily_driver.model}. "
      f"It uses {daily_driver.fuel} and has {daily_driver.number_of_wheels} wheels.")

truck = Truck("Ford", "F350")
print(f"I also have a {truck.make} {truck.model}. "
      f"It uses {truck.fuel} and has {truck.number_of_wheels} wheels.")


