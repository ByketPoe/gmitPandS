# extra.py
# The purpose of this program is to show off ;)
# author: Emma Farrell

# The expression below tries to concatenate data of different types, in this case, strings and integers. 
# They need to be of the same data type so that the program knows how to add them together.
# message = 'I have eaten ' + 99 + ' burritos'
# print(message)

# The code corrected would be:
message = 'I have eaten ' + str(99) + ' burritos'
print(message)

# This also works
message = 'I have eaten 99 burritos'
print(message)