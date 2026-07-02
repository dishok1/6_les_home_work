class Rectangle:
    """Class create object Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rect1 = Rectangle(width=7, height=100)

rect2 = Rectangle(width=2.3, height=4)

area1 = rect1.calculate_area()
area2 = rect2.calculate_area()

print(f"The area of the first rectangle is: {area1}")
print(f"The area of the second rectangle is: {area2}")
