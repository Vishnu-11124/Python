
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def type_of_vehicle(self):
        return f"{self.make} {self.model} is a petrol car."

class ElectricCar(Car):
    def type_of_vehicle(self):
        return f"{self.make} {self.model} is an electric car."


honda = Car("Honda", "Civic")
tesla = ElectricCar("Tesla", "Model S")

print(honda.type_of_vehicle())  # Output: Honda Civic is a petrol car.
print(tesla.type_of_vehicle())  # Output: Tesla Model S is an electric car.