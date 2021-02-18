# convert.py
# The purpose of this program is to convert dollars to cents.
# The program ensures that the returned result is positive. 
# author: Emma Farrell

# The user is asked for the cash amount.
# The input() function is used to take in the amount from the user.
# This is cast to a float and assigned to a variable "inputAmount".
# It is cast to a float because it needs to include two decimal places for the cents.
inputAmount = float(input("Please enter the amount: "))

# The abs() function is used to find the absolute value of the amount inputted.
# This will ensure that if the user is in debt, this will not affect the result.
# The result is assigned to the variable "absInputAmount"
absInputAmount = abs(inputAmount)

# The result is converted to cents by multiplying by 100.
# It is converted to an int as money is not dealt with in fractions of cents. 
# The result is assigned to the variable "absInCents"
amountInCents = int(absInputAmount*100)

# The result is printed using .format() and print() functions.
print("The amount in cents is: {}".format(amountInCents))