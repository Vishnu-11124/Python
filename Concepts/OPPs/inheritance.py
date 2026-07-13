class CarData:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class ElectricCarData(CarData):
    def __init__(self, brand, model, battery_size, recharge_time):
        super().__init__(brand, model)
        self.battery_size = battery_size
        self.recharge_time = recharge_time

my_car = ElectricCarData("Tesla", "Model S", "85WH", "1hr")

print(my_car.recharge_time)
my_car.display_info()

# ---------------------------------------------------------------
# Multi-level inheritance

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class ElectricCar(Car):
    def __init__(self, brand, model, seats, battery_size):
        super().__init__(brand, model, seats)
        self.battery_size = battery_size

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}, Battery Size: {self.battery_size}")

tesla = ElectricCar("Tesla", "Model 3", 5, "75kWh")
tesla.display_info()        

# ---------------------------------------------------------------


