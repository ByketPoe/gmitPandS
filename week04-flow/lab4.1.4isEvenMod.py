# isEvenMod.py
# The purpose of this program is to use modulus and if statements to determine if a number is odd or even.
# author: Emma Farrell

# This statement initialises the value for number to be used in the sentinal loop, as well as taking in the number to be evaluated.
# The user is warned that entering -1 will quit the program. 
number = int(input("Enter a whole number (-1 to quit): "))

# The while loop evaluates the input and executes the code so long as the user didn't enter -1.
while number != -1:
    # The code evaluating if the number is odd or even remains unchanged from the original.
    if (number % 2) == 0:
        print("{} is an even number".format(number))
    else:
        print("{} is an odd number".format(number))
    
    # The user is again asked to enter a number and instructed on how to quit the program.
    # If this was not here, number would never be updated and the while loop would execute infinitely.
    number = int(input("Enter a whole number (-1 to quit): "))
