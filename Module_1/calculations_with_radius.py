"""
File: calculations__with_radius
Author: Marki Lyons
Date: 2023-10-29
Description: This is a program that will calculate and display the circumference and area of a circle, 
as well as the volume of a sphere, based on user input of a radius.

"""
import math
from time import sleep

print("Hi there! Let's do some calculations based on the radius of a circle or sphere. \n")

radius = float(input("Please enter a radius: "))
print()
sleep(1.0)

print(f"You entered {radius} as the radius, so let's get started. \n")
sleep(1.0)

def calc_circumference():
    circumference = 2*math.pi*radius
    print(f"The circumference of a circle with a radius of {radius} is {circumference} \n")

calc_circumference()
sleep(1.5)

def calc_area():
    area = math.pi*radius**2
    print(f"The area of a circle with a radius of {radius} is {area} \n")

calc_area()
sleep(1.5)

def calc_volume():
    volume = 4/3*math.pi*radius**3
    print(f"The volume of a sphere with a radius of {radius} is {volume} \n")

calc_volume()
sleep(1.2)

print("Great job! I hope you enjoyed making these calculations!")