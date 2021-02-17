# normalise.py
# The purpose of this program is to take a string input and output it with leading and trailing spaces removed and all lowercase letters
# author: Emma Farrell

# The user is asked to enter some text. This is assigned to the variable "rawString".
# No need to cast as the text is input as a string.
rawString = input("Please enter some text: ")

# The string has leading and trailing spaces removed using the .strip() function.
# The characters are converted to lowercase using the .lower() function.
# The resulting string is assigned to the variable normalisedString
normalisedString= rawString.strip().lower()

# The lengths of the original raw string and stripped string are calculated using the len() function, 
# The result is assigned to variables.
lengthOfRawString = len(rawString)
lengthOfNormalisedString = len(normalisedString)

# The results are printed.
print("Your text normalised is: {}".format(normalisedString))
print("We have reduced the input text from {} to {}".format(lengthOfRawString, lengthOfNormalisedString))