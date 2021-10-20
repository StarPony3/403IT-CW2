
# Parent class 'Calculations'
class Calculations:
    '''calss containing mathematical calculations'''


    # Constructor method
    def __init__(self, a, b = None):        
        self.a = a
        self.b = b

    
    # Method for adding two values
    def addition(self):
        return (f"The sum of {self.a} and {self.b} is {self.a + self.b}")


    # Method for subtracting two values
    def subtraction(self):
        return (f"{self.b} subtracted from {self.a} is {self.a - self.b}")


    # Method for multiplying two values
    def multiplication(self):
        return self.a * self.b

    
    # Method for calculating the area of a circle
    def circle_area(self): 
        radius_squared = self.a ** 2            
        c = radius_squared * 3.142
        return (f"The area of a circle with {self.a}cm radius is {c}cm\u00b2")


    
class Shapes(Calculations):
    '''class for calculating area of shapes'''           
    
    # Method overriding the parent 'multiplication' method.
    def rectangle_area(self):
        return ("The area of this rectangle is {}cm\u00b2".format(Calculations.multiplication(self)))

    # Method overriding the parent 'circle_area' method.
    def circle_area_input(self):
        return Calculations.circle_area(self)
        

# Calling methods from parent class
d = Calculations(8, 6)
print (d.addition())


e = Calculations(2, 4)
print (e.subtraction())


f = Calculations(10, 12)
print (f.multiplication())


g = Calculations(5)                             
print (g.circle_area())       


# Calling methods from child class
h = Shapes(8, 6)
print (h.rectangle_area())

j = Shapes (int(input("Enter number:")))
print (j.circle_area())

