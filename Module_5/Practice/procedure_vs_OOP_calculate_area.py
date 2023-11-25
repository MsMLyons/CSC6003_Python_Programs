# Procedural approach
def calculate_rectangle_area(length, width):
    area = length * width
    return area

length = 5
width = 3
rectangle_area = calculate_rectangle_area(length, width)
print(rectangle_area)

# output --> 15


# OOP approach
class Rectangle:
    def __init(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area
    
length = 7
width = 2
rectangle = Rectangle(length, width)
rectangle_area = rectangle.calculate_area()
print(rectangle_area)

# output --> 14