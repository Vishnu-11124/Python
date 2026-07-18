class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department} and Salary: {self.salary}")    

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 75000)

kiran = Employee("Hr Trainee", "Hr", 20000)
kiran.showDetails()

hari = Engineer("Hari", 25)
hari.showDetails()