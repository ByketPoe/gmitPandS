# absolute.py
# The purpose of this program is to give the absolute value of a number. 
# author: Emma Farrell

# The input() function is used to take in a number from the user.
# It is unclear what type of number is required, I will assume a float, as this takes into account a wider variety of numbers.
# This is cast to a float and assigned to a variable "numberRaw".
numberRaw = float(input("Enter a number: "))

# The abs() function is used to get the absolute value of the input number.
# The result is assigned to the variable "numberAbsoluteValue".
numberAbsoluteValue = abs(numberRaw)

# The result is printed using .format() and print(). 
print('The absolute value of {} is {}'.format(numberRaw, numberAbsoluteValue))