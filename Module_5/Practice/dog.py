# Create a class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking!")

# Create objects
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Call the methods
dog1.bark() # output --> Buddy is barking!
dog2.bark() # output --> Max is barking!