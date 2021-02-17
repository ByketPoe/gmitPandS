# randomFruit.py
# The purpose of this program is to print a random fruit name.
# author: Emma Farrell

# The random module is imported.
# This will be necessary to use a function to generate a random number.
import random

# A list consisting of strings is created and assigned to the variable fruits.
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

# The randint() function is used to generate a number between 0 and the length of the fruits list minus 1.
# List indexes start at 0, therefore the last list item will have an index of the length of the list minus 1.
# The result is assigned to a variable. 
# The number generate will be used as the index of the fruits list to choose the fruit.
index = random.randint(0, len(fruits)-1)

# The string at list position "index" of the fruits list is assigned to the variable "fruit".
fruit = fruits[index]

# The result is printed. 
print('A Random Fruit: {}'.format(fruit))