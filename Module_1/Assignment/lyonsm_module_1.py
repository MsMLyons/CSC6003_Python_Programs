"""
File: lyonsm_module_1
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 1
Date Created: 2023-10-29
Date Updated: 2023-10-31
Description: This is a program that will calculate and display the circumference and area of a circle, 
as well as the volume of a sphere, based on user input of a radius.

"""
import math

radius = float(input("Please enter a radius: \n\n"))
print()

if radius > 0: 
    def calc_circumference():
        """ Circumference Function """
        circumference = 2*math.pi*radius
        circumference_txt = "The circumference of a circle with a radius of {:.3f} is {:.7} \n"
        print(circumference_txt.format(radius, circumference))        

    def calc_area():
        """ Area Function """
        area = math.pi*radius**2
        area_txt = "The area of a circle with a radius of {:.3f} is {:.7} \n"
        print(area_txt.format(radius, area))    

    def calc_volume():
        """ Volume Function """
        volume = 4/3*math.pi*radius**3
        volume_text = "The volume of a sphere with a radius of {:.3f} is {:.7} \n"
        print(volume_text.format(radius, volume))

    calc_circumference()
    calc_area()
    calc_volume()
else:
    print("Please try again using a value greater than zero.")