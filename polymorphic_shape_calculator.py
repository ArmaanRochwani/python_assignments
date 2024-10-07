import math  # Base class for all shapes

class Shape:
    def area_is(self):  # Method to calculate area and overridden in subclasses
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter_is(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):  # Subclass for Circle, inherits from Shape
    def __init__(self, radius):
        self.radius = radius  # Initialize the circle with its radius

    def area_is(self):  # Calculate the area of the circle
        return math.pi * self.radius ** 2

    def perimeter_is(self):  # Override method to calculate the perimeter of the circle
        return 2 * math.pi * self.radius

class Rectangle(Shape):  # Subclass for Rectangle, inherits from Shape
    def __init__(self, length, width):
        self.length = length  # Initialize the rectangle with its length and width
        self.width = width

    def area_is(self):  # Override method to calculate area of the rectangle
        return self.length * self.width

    def perimeter_is(self):  # Function to calculate perimeter
        return 2 * (self.length + self.width)

class Triangle(Shape):  # Subclass for Triangle, inherits from Shape
    def __init__(self, side1, side2, side3):
        self.side1 = side1  # Initialize the triangle with its three sides
        self.side2 = side2
        self.side3 = side3

    def area_is(self):  # Override method to calculate the area of the triangle using Heron's formula
        a, b, c = self.side1, self.side2, self.side3
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def perimeter_is(self):
        return self.side1 + self.side2 + self.side3

# Function to ensure input is positive 
def get_positive_float(input_from_user):
    while True:
        try:
            value = float(input(input_from_user))
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(e)

def main():
    shapes = []  # List to store different shapes created by the user
    print("Select shapes to create (Enter 'satisfied' when finished):")
    
    while True:  # Loop until user enters 'satisfied'
        shape_type = input("Enter shape type (Circle, Rectangle, Triangle): ").strip().lower()
        if shape_type == 'satisfied':
            break
        elif shape_type == 'circle':
            radius = get_positive_float("Enter radius: ")  # Get valid radius
            shapes.append(Circle(radius))
        elif shape_type == 'rectangle':  
            # Get valid length and width
            length = get_positive_float("Enter length: ")
            width = get_positive_float("Enter width: ")
            shapes.append(Rectangle(length, width))
        elif shape_type == 'triangle':
            side1 = get_positive_float("Enter side 1: ")
            side2 = get_positive_float("Enter side 2: ")
            side3 = get_positive_float("Enter side 3: ")
            if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
                shapes.append(Triangle(side1, side2, side3))
            else:  # Checking triangle’s inequality theorem
                print("Invalid triangle sides. The sum of any two sides must be greater than the third.")
        else:
            print("Invalid shape type. Please enter Circle, Rectangle, Triangle or 'satisfied'.")

    for shape in shapes:  # Loop through each shape and display its area and perimeter
        print(f"\nArea of {shape.__class__.__name__}: {shape.area_is():.2f}")
        print(f"Perimeter of {shape.__class__.__name__}: {shape.perimeter_is():.2f}")

if __name__ == "__main__":  # Program starts from here
    main()
