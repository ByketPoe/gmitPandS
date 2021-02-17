# randomFruit2.py
# The purpose of this program is to print a random fruit name from a tuple consisting of fruits.
# author: Emma Farrell

# The random module is imported.
# This will be necessary to use a function to generate a random number.
import random

# A tuple consisting of strings is created and assigned to the variable fruits.
fruits =('Apple', 'Orange', 'Banana', 'Pear')

# The randint() function is used to generate a number between 0 and the length of the fruits tuple minus 1.
# Indexes start at 0, therefore the last tuple item will have an index of the length of the tuple minus 1.
# The result is assigned to a variable. 
# The number generated will be used as the index of the fruits tuple to choose the fruit.
index = random.randint(0, len(fruits)-1)

# The string at tuple position "index" of the fruits tuple is assigned to the variable "fruit".
fruit = fruits[index]

# The result is printed. 
print('A Random Fruit: {}'.format(fruit))

# Using the choices function from the random module instead to find the random fruit.
# The argument k defines the length of the returned list. 
# This function also works when selecting from a tuple. 
print('Another random fruit: {}'.format(random.choices(fruits, k=1)))