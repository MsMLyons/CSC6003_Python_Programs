""" 
File: lyonsm_module_4.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 3
Date Created: 2023-11-20
Date Updated: 2023-11-21

Description: 

This program creates two classes. The Rectangle class is the 
parent class, from which the Parallelepiped child class inherits 
the attributes of length and width. 

The Rectangle class initializes these attributes via user input, 
then uses the input data to calculate the perimeter and area of a 
rectangle. Before passing that information onto its child class, the 
results of the input and calculations are displayed for the user. 

The Parallelepiped class takes advantage of inheritance by re-
utilizing user input of length and width, then prompts the user for
the shape's height. With this data, it calculates the volume of the
shape and prints the results for the user. 
"""

class Rectangle():
    """ Rectangle class with length and width attributes. This class calculates the 
        perimeter and area of a rectangle based on user input of length and width.
    """
    def __init__(self):
        """ Prompts the user for input and creates a rectangle """
        print("\nHello! Let's calculate the perimeter and area of a rectangle.\n")
        # assign user input to the attributes of the rectangle
        self.length = int(input("Please enter an integer for the rectangle length: "))
        self.width = int(input("Now enter an integer for the rectangle width: "))

    def perimeter(self):
        """ Calculates the perimeter of the rectangle """
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def area(self):
        """ Calculates the area of the rectangle """
        area = self.length * self.width
        return area

    def display(self):
        """ Displays the length, width, perimeter and area of a rectangle object """
        print("\nThe length of the rectangle is:", self.length)
        print("The width of the rectangle is:", self.width)
        print("\nThe perimeter of the rectangle is:", self.perimeter())
        print("The area of the rectangle is:", self.area())        

class Parallelepiped(Rectangle):
    """ The Parallelepiped class inherits from the Rectangle class. """
    def __init__(self):
        """ Reuses previous user input and prompts for the height of the parallelepiped """
        print("\nGreat! Now let's calculate the volume of a parallelepiped.")
        print("We'll base it on the same length and width of the rectangle.\n")
        # reassign inherited attributes to be used in this class
        self.length = rectangle_instance.length 
        self.width = rectangle_instance.width
        # assign user input to the new attribute needed for the parallelepiped shape
        self.height = int(input("You just need to add the height of parallelepiped: "))

    def volume(self):
        """ This method calculates and prints the volume of the parallelepiped """
        volume = self.length * self.width * self.height
        print("\nThe volume of the Parallelepiped is:", volume)
        print("Well done! I hope you enjoyed making these calculations. Goodbye!")
        return volume
    
if __name__ == "__main__":
    rectangle_instance = Rectangle()
    rectangle_instance.display()
    parallelepiped = Parallelepiped()
    parallelepiped.volume()