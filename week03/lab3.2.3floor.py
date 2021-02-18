# floor.py
# The purpose of this program is to return a rounded number. 
# The returned number will be rounded down e.g. 4.9 will become 4.
# author: Emma Farrell

# The math module is imported. This is required to used the floor() function
import math

# The input() function is used to take in a number from the user.
# This is cast to a float and assigned to a variable "numberToFloor".
numberToFloor = float(input("Enter a float number: "))

# The floor() function is used to round down the input number. 
# The result is assigned to the variable "flooredNumber".
flooredNumber = math.floor(numberToFloor)

# The result is printed using .format() and print(). 
print('{} rounded down (floored) is {}'.format(numberToFloor, flooredNumber))