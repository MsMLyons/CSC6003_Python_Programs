class Rectangle():
    """ Rectangle class with length and width attributes.
        This class calculates the perimeter and area of a
        rectangle based on user input of length and width.
    """
    def __init__(self):
        """ Prompts the user for input and creates a rectangle """
        print("\nHello! Let's calculate the perimeter and area of a rectangle.\n")
        self.length = int(input("Please enter an integer for the rectangle length: "))
        self.width = int(input("Now enter an integer for the rectangle width: "))

    def perimeter(self):
        """ Calculate the perimeter of the rectangle """
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def area(self):
        """ Calculate the area of the rectangle """
        area = self.length * self.width
        return area

    def display(self):
        """ Display the length, width, perimeter and area of a rectangle object """
        print("\nThe length of the rectangle is:", self.length)
        print("The width of the rectangle is:", self.width)
        print("\nThe perimeter of the rectangle is:", self.perimeter())
        print("The area of the rectangle is:", self.area())        

class Parallelepiped(Rectangle):
    """ The Parallelepiped class inherits from the Rectangle class. 
        It reuses previous user input and prompts for the height
        of the parallelepiped to calculate the volume of the shape.
    """
    def __init__(self):
        print("\nGreat! Now let's calculate the volume of a parallelepiped.")
        print("We'll base it on the same length and width of the rectangle.\n")
        self.length = rectangle.length 
        self.width = rectangle.width
        self.height = int(input("You just need to add the height of parallelepiped: "))

    def volume(self):
        """ This method calculates and prints the volume of the parallelepiped """
        volume = self.length * self.width * self.height
        print("\nThe volume of the Parallelepiped is:", volume)
        print("Well done! I hope you enjoyed making these calculations. Goodbye!")
        return volume
    
rectangle = Rectangle()
rectangle.display()
parallelepiped = Parallelepiped()
parallelepiped.volume()