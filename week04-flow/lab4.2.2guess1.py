# guess1.py
# The purpose of this program is to ask the user to correctly guess a number.
# The program will execute until the user has guessed the correct number. 
# author: Emma Farrell

# "numberToGuess" and "guess" variables are intitiated. 
numberToGuess = 30
guess = int(input("Please guess the number: "))

# The while loop evaluates the input and executes the code within the loop so long as the user didn't enter 30.
while guess != numberToGuess:
    # The loop will continue to tell the user that their guess was wrong and ask the user for another number until they successfully guess the correct number. 
    print("Wrong")
    # This line asks for input again and updates the value of the variable "guess", ensuring that the loop won't execute infinitely.
    guess = int(input("Please guess again: "))

# The code will only reach this statement once the user has guessed the correct number and broken out of the while loop.
print("Well done! Yes, the number was", numberToGuess)