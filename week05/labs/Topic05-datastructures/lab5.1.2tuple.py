# tupleMonths.py
# The purpose of this program is to print the months of the summer from a tuple that contains all of the months of the year.
# author: Emma Farrell

# A tuple is created and assigned to the variable "months". 
# This contains twelves strings that give the names of the months of the year.
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Slicing is used to extract a selection of the months from the tuple "months".
# The items at indexes 4, 5 and 6 are assigned as a list to the variable "summer".
# Slicing does not include the item at the last index defined i.e. the item at index 7 is not included.
summer = months[4:7]
# A for loop loops through the items in the list "summer" and prints them one at a time.
for month in summer:
    print(month)