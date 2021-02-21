# isEven.py
# The purpose of this program is to use modulus and if statements to determine if a number is odd or even.
# author: Emma Farrell

# I prefer to use phrases like "text" or "whole number" instead of "string" and "integer" as I beleive they are more user friendly.
number = int(input("Enter a whole number: "))

# Modulus (%) is used to calculated the remainder of the input number divided by 2.
# The if statement evaluates if the remainder is equal to 0.
# If true, the number is even and a message to indicate this is printed.
# Otherwise, the number is odd and the message diplayed will state that it is odd. 
if (number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))