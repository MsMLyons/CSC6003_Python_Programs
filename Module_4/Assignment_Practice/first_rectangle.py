# Write a Rectangle class in Python language, 
# allowing you to build a rectangle with 
# length and width attributes.

class Rectangle():
    """ Rectangle class with length and width attributes """
    def __init__(self):
        """ Creates a Rectangle """
        self.length = 0
        self.width = 0

# Create a Perimeter() method to calculate 
# the perimeter of the rectangle and a Area() 
# method to calculate the area of the rectangle.

    def perimeter(self):
        """ Calculates the perimeter of the rectangle """
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def area(self):
        """ Calculates the area of the rectangle """
        area = self.length * self.width
        return area

# Create a method display() that displays 
# the length, width, perimeter and area of 
# an object created using an instantiation 
# on rectangle class.

    def display(self):
        """ Display the length, width, perimeter and area of a rectangle object """
        print("The length of the rectangle is:", self.length)
        print("The width of the rectangle is:", self.width)
        print("The perimeter of the rectangle is:", self.perimeter())
        print("The area of the rectangle is:", self.area())        

# Create a Parallelepiped child class 
# inheriting from the Rectangle class and with 
# a height attribute and another Volume() 
# method to calculate the volume of the Parallelepiped.

class Parallelepiped(Rectangle):
    """ The Parallelepiped class inherits from the Rectangle class """
    def __init__(self):
        self.height = 0

    def volume(self):
        """ This method calculates the volume of the parallelepiped """
        volume = self.length * self.width * self.height
        print("The volume of the Parallelepiped is:", volume)
        return volume

rectangle = Rectangle()
rectangle.length = 4
rectangle.width = 3
rectangle.display()
parallelepiped = Parallelepiped()
parallelepiped.length = 5
parallelepiped.width = 2
parallelepiped.height = 3
parallelepiped.volume()


