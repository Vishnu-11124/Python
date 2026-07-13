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

# -----------------------------------------------------------------

class Student:
    college_name = "ABC College"  # Class variable

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def set_marks(self, tenth_marks, twelfth_marks):
        self.tenth_marks = tenth_marks
        self.twelfth_marks = twelfth_marks

    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, 10th Marks: {self.tenth_marks}, 12th Marks: {self.twelfth_marks}, College: {self.college_name}")


student1 = Student("Alice", 101)
student1.set_marks(85, 90)
student1.display_info()