class CarData:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")    


car1 = CarData("BMW", "X3")    
car1.display_info()

car2 = CarData("Toyota", "Innova")
car2.display_info()