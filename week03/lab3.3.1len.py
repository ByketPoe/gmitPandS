# len.py
# The purpose of this program is to provide the character count of some text.
# author: Emma Farrell

# The input() function is used to take in the amount from the user.
# This is assigned to a variable "inputString".
# No need to cast the input as we require it to be a string.
inputString = input('Please enter some text: ')

# The length of the string is calculated by the len() function and assigned to the variable "lengthOfString".
# I am assuming that the user wants to have leading and trailing spaces counted, so I have not sued the strip() function.
# Internal spaces will also be counted. 
lengthOfString = len(inputString)

# The result is printed using .format() and print() functions.
print('The length of "{}" is {}'.format(inputString, lengthOfString))