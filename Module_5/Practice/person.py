class Person:
    # Constructor method with parameters for name & age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Alice", 25)

# Access the object's attributes
print(person1.name)
print(person1.age)

# Call a method on the object
person1.say_hello()

# output -->
    # Alice
    # 25
    # Hello, my name is Alice and I am 25 years old.