# topThree.py
# The purpose of this program is to randomly generate 10 numbers, print them all, then print out the highest 3 values.
# author: Emma Farrell

# Because this program requires randomly generated numbers, the random module is imported.
import random

howMany     = 10
topHowMany  = 3
rangeFrom   = 0
rangeTo     = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom, rangeTo))

print("{} random numbers\t {}".format(howMany, numbers))

topOnes = numbers.copy()
topOnes.sort(reverse=True)
print("The top {} are \t\t {}".format(topHowMany, topOnes[0:topHowMany]))