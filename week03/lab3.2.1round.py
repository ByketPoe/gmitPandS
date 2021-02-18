# round.py
# The purpose of this program is to round a number.
# It rounds to the nearest number, so caution is advised if accuracy is required.
# author: Emma Farrell

# The input() function is used to take in a number from the user.
# This is cast to a float and assigned to a variable "numberToRound".
numberToRound = float(input("Enter a number of type float: "))

# The round() function is used to round the input number. 
# The Result is assigned to the variable "roundedNumber".
roundedNumber = round(numberToRound)

# The result is printed using .format() and print(). 
print('{} rounded is {}'.format(numberToRound, roundedNumber))