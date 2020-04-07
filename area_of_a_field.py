# Taking input from the user in feets
width = float(input("Input the width in feets: "))
length = float(input("Input the length in feets: "))
# Finding the area
square_feet = width * length
acre = square_feet/43560
# Showing the area to the user
print("The area of the farm is", acre, "acre")