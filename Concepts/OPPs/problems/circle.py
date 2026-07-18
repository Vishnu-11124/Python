class Circle:
    pi = 22/7
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return self.pi * self.radius ** 2   
    
    def perimeter(self):
        return 2 * self.pi *self.radius
    
c1 = Circle(21)
print("Area of Circle: ", c1.area())    
print("Perimeter of Circle: ", c1.perimeter())