import math

print("Hi there! Let's do some calculations based on the radius of a circle or sphere. \n")

radius = float(input("Please enter a radius: "))

print(f"You entered {radius} as the radius, so let's get started. \n")
print("First we'll calculate the circumference of a circle. \n")

def calc_circumference():
    circumference = 2*math.pi*radius
    print(f"The circumference of a circle with a radius of {radius} is {circumference} \n")

calc_circumference()

print("Now let's calculate the area of the circle. \n")

def calc_area():
    area = math.pi*radius**2
    print(f"The area of a circle with a radius of {radius} is {area} \n")

calc_area()

print("Now let's calculate the volume of a sphere based on the radius you entered. \n")

def calc_volume():
    volume = 4/3*math.pi*radius**3
    print(f"The volume of a sphere with a radius of {radius} is {volume} \n")

calc_volume()

print("Great job! I hope you enjoyed making these calculations!")
