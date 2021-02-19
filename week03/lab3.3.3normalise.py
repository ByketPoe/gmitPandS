# normalise.py
# The purpose of this program is to output a string with leading and trailing spaces stripped and all characters in lowercase.
# This program also returns the length of the input and output string.
# author: Emma Farrell

# The input() function is used to take in some text from the user.
# This is assigned to a variable "rawString".
# No need to cast the input as we require it to be a string.
rawString = input("Please enter some text: ")

# The .strip() function removes all spaces at the beginning and end of the string. Spaces between letters are not removed.
# The .lower() function converts any uppercase letters to lowercase.
# The resulting string from the two functions is passed to the variable "normalisedString".
normalisedString = rawString.strip().lower()

# The len() function is used to get the length of the input string and the normalised string. 
# The results are assigned to the variables "lengthOfRawString" and "lengthOfNormalisedString".
lengthOfRawString = len(rawString)
lengthOfNormalisedString = len(normalisedString)

# The results are printed using .format() and print() functions.
print("That text normalised is: {}".format(normalisedString))
print("We reduced the input text from {} to {}!".format(lengthOfRawString, lengthOfNormalisedString))