# randomGenerator.py
# The purpose of this program is to print out a random number between 1 and 10.
# author: Emma Farrell

# Import the random module. 
# This will be necessary to use a function to generate a random number.
import random

# Generate a random number between 1 and 10 using the .randint() function.
# The two numbers represent the max and min numbers in the range.
# Assign the result to the variable "number".
number = random.randint(1,10)

# Print the result.
print("here is a random number: {}".format(number))