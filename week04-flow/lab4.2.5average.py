# average.py
# The purpose of this program is to collect numerical data entered by the user and calculate the average.
# author: Emma Farrell

# An empty list is created and assigned to a variable "numbers"
numbers = []

# The user is asked to enter a number, which is cast to a float and assigned to the variable "number".
# I have decided to use floats for the input instead of ints to enable to user to evaluate a greater amount of numbers.
number = float(input("Enter a whole number (0 to quit): "))

# A while loop checks if the user entered 0. If not, the code within the loop is executed.
while number != 0:
    # The number the user entered is added to the list "numbers"
    numbers.append(number)

    # The user is asked for another number. 
    # This will be evaluated at the start of the while loop again to see if it is equal to 0.
    number = float(input("Enter another whole number (0 to quit): "))

# The for loop iterates through the entries in the list "numbers".
# "values" is a temporary variable used to denote the current item in the list being iterated over.
# This changes each iteration to be the next item in the list. 
for value in numbers:
    # The current value of "value" is printed.
    print(value)

# If the user enters 0 the first iteration of the while loop, then the length of the list will be 0.
# This will cause a divide by 0 error when calculating the average.
# To resolve this, I have added an if statement to check the length of the list. 
# If the length of the list is 0, it will append 0 to the list. This ensures that the sum will be zero, giving an average of 0. 
if len(numbers) == 0:
    numbers.append(0)

# The average is calculated. First, the sum() function calculates the sum of the values in the list numbers.
# This result is cast as a float. 
# If all of the values are ints, the result will be an int automatically, but as we are dividing, we want to maintain it as a float.
# This gives a more precise result.
# The length of the list is obtained using the len() function because this tells us how many values there are.
# The sum of the values is divided by the number of values to obtain the average. Float division is used (/) to ensure the result is a float.
# The result is assigned to the variable "average".
average = float(sum(numbers)) / len(numbers)

# The result is printed.
print("The average is {}".format(average))