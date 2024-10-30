import math

# Base class
class Shape:
    def area(self):
        pass  # Placeholder for area calculation

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Function that uses polymorphism
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Create instances of Circle and Rectangle
circle = Circle(5)      # Circle with radius 5
rectangle = Rectangle(4, 6)  # Rectangle with width 4 and height 6

# Call the same method for both shapes
print_area(circle)      # Outputs: The area is: 78.53981633974483
print_area(rectangle)   # Outputs: The area is: 24
