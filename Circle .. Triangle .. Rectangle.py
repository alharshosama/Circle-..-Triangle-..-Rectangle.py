##اسامة محمد صالح الهرش

import math

class Shape:
    def perimeter(self):
        pass
    
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def area(self):
        # Using Heron's formula to calculate the area of a triangle
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width

def main():
    # Create instances of different shapes
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(4, 6)
    
    # Calculate and display the perimeter and area of each shape
    print("Circle:")
    print("Perimeter:", circle.perimeter())
    print("Area:", circle.area())
    
    print("\nTriangle:")
    print("Perimeter:", triangle.perimeter())
    print("Area:", triangle.area())
    
    print("\nRectangle:")
    print("Perimeter:", rectangle.perimeter())
    print("Area:", rectangle.area())

if __name__ == '__main__':
    main()

