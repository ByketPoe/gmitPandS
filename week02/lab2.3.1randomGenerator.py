# randomGenerator.py
# The purpose of this program is to print out a random number between user inputted numbers.
# author: Emma Farrell

# The random module is imported.
# This will be necessary to use a function to generate a random number.
import random

# The user is asked for two numbers. These will be the range in which the random number will be chosen.
# The numbers are cast as ints and assigned to variables.
minNumber = int(input("Please enter the range minimum: "))
maxNumber = int(input("Please enter the range maximum: "))

# A random number between the numbers inputted by the user is generated using the .randint() function.
# The two numbers represent the max and min numbers in the range.
# The result is assigned to the variable "number".
number = random.randint(minNumber, maxNumber)

# The result is printed.
print("Here is a random number between {} and {} : {}".format(minNumber, maxNumber, number))