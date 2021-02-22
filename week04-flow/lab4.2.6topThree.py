# topThree.py
# The purpose of this program is to randomly generate 10 numbers, print them all, then print out the highest 3 values.
# author: Emma Farrell

# Because this program requires randomly generated numbers, the random module is imported.
import random

# Variables that control how many numbers will be generated, how many numbers from the top will be selected 
# and the min and max range for the random number generation are initialised and set to values.
howMany     = 10
topHowMany  = 3
rangeFrom   = 0
rangeTo     = 100

# An empty list is created to store the numbers that will be randomly generated.
numbers = []

# A for loop iterates 10 times. 
# This is controlled by the range function, which defines the number of iterations.
# In the first iteration, i will equal 0, then 1 on the next iteration etc. up to but not including 10.
# This causes the code in the loop to execute 10 times.
for i in range(0, howMany):
    # random.randint() picks a random number between the variables defined earlier in the code.
    # This number is appended to the numbers list using the .append() function.
    numbers.append(random.randint(rangeFrom, rangeTo))

# After the loop has terminated, the amount of numbers generated and the full list of numbers is printed. 
print("{} random numbers\t {}".format(howMany, numbers))

# The .sort() function sorts the values according to value.
# The argument reverse=True sorts the values in reverse order from largest to smallest.
numbers.sort(reverse=True)

# The top 3 values are printed by slicing the first three values from the (now sorted) list numbers.
print("The top {} are \t\t {}".format(topHowMany, numbers[0:topHowMany]))