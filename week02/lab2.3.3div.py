# div.py
# The purpose of this program is to show the result and remainder of dividing two numbers
# author: Emma Farrell

# The input fuctions ask the user to input two numbers. 
# This numbers are input as strings
# They must be cast as an integer using the int() function before the program can perform mathematical operations on it
numerator = int(input("Enter the first number: "))
divisor = int(input("Enter the number you want to divide by: "))

# The numerator is divided by the divisor using the // operator.
# // provides an integer answer by rounding the result down. 
# The result is assigned to the variable answer.
answer = numerator // divisor # In the lab notes, this was cast to an int, but I see no reason to do so when the dividing operator alreadys rounds the number

# The remainder is calculated by using the modulus operator %
# The result of this is assigned to the variable remainder.
remainder = numerator % divisor

# The result is printed with the format() function used to insert the variables within the string
print("{} divided by {} is {} with remainder {}".format(numerator, divisor, answer, remainder))