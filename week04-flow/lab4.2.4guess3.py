# guess3.py
# The purpose of this program is to ask the user to correctly guess a randomly number.
# The program will execute until the user has guessed the correct number. 
# This modified version will check the user's guess and let them know if their guess is too high or too low.
# author: Emma Farrell

# Because this program requires a randomly generated number, the random module is imported.
import random

# "numberToGuess" and "guess" variables are intitiated. 
# "numberToGuess" is generated randomly using the random.randint() function.
# It randomly generates a number between 0 and 100.
numberToGuess = random.randint(0, 100)
guess = int(input("Please guess the number: "))

# The while loop evaluates the input and executes the code within the loop so long as the user didn't enter 30.
while guess != numberToGuess:
    # An if statement evaluates if the number the user inputted is less than the number to guess.
    if guess < numberToGuess:
        # If true, the program prints a message telling them that their guess was too low. 
        # Otherwise, this code is skipped over.
        print("Too low!")
    else: # The only other scenario is that the number is too high, as the while loop already checked to see if the number was correct.
        # No need for an elif statement, just print that the number was too high. 
        print("Too high!")

    # This line asks for input again and updates the value of the variable "guess", ensuring that the loop won't execute infinitely.
    guess = int(input("Please guess again: "))

# The code will only reach this statement once the user has guessed the correct number and broken out of the while loop.
print("Well done! Yes, the number was", numberToGuess)