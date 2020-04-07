# importing math module, to use pi
from math import * 
# Taking input from the user
radius = float(input("Input the radius: "))
height = float(input("Input the height: "))
# Doing the math
area_of_circular_base = pi * (radius ** 2)
area = area_of_circular_base * height
# Printing out the result
print("The surface area is", round(area, 1), "units squared")