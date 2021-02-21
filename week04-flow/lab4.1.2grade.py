# grade.py
# The purpose of this program is to provide a grade based on the input percentage. 
# author: Emma Farrell

# The percentage is requested from the user and converted to a float. 
# Float is appropriate in this occasion as we do not want people to fail based on rounding to an integer.
percentage = float(input("Enter the percentage: "))

# First, it is checked that the percentage is valid using the initial if statement with an or operator.
# Any value outside of the range 0-100 is not a percentage and is therefore not valid.
# "or" is suitable as it evaluates each statement separately, if only one is true than the whole statement is true and the percentage is not valid.
# The elif statements and else statement check what grade bracket the percentage falls into.
# Depending on the value of the percentage, the program will print the result.
# It is important to start the check with the lowest percentage bracket and work upwards. 
# This is because technically, a number like 39 is less than both 40 and 50. 
# By checking if it is less than 40 first, we can skip the rest of the evaluations, and the correct grade bracket is printed.
if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 1")
elif percentage < 70:
    print("Merit 2")
else:
    print("Distinction")