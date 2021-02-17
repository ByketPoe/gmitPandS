# sub.py
# The purpose of this program is to subtract one number from another.
# author: Emma Farrell

# The input fuctions ask the user to input two numbers. 
# This numbers are input as strings
# They must be cast as an integer using the int() function before the program can perform mathematical operations on it
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# The result of subtracting the second number from the first number is calculted
# The result is printed with the format() function used to insert the variables within the string
answer = number1 - number2
print("{} minus {} is {}".format(number1, number2, answer))

# Errors occur when the user tries to enter a float or a string.
# The program is able to calculate minus numbers