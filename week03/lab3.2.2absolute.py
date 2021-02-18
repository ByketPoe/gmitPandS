# absolute.py
# The purpose of this program is to give the absolute value of a number. 
# author: Emma Farrell

# The input() function is used to take in a number from the user.
# It is unclear what type of number is required, I will assume a float, as this takes into accound a wider variety of numbers.
# This is cast to a float and assigned to a variable "numberRaw".
numberRaw = float(input("Enter a number: "))

# The round() function is used to round the input number. 
# The Result is assigned to the variable "roundedNumber".
numberAbsoluteValue = abs(numberRaw)

# The rsult is printed using .format() and print(). 
print('The absolute value of {} is {}'.format(numberRaw, numberAbsoluteValue))