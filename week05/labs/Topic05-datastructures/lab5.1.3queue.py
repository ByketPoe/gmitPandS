# queue.py
# The purpose of this program is to 
# author: Emma Farrell

# The random module is imported.
# This will be necessary to use a function to generate a random number.
import random

# Three variables are defined and their values are set. 
# "queue" is an empty list that will hold all of the numbers in the queue.
# "numberOfNumbers" is an integer that will define how many numbers are added to the queue.
# "rangeTo" is an integer that will define the upper limit of the random numbers that can be generated.
queue = []
numberOfNumbers = 10
rangeTo = 100

# A for loop iterates 10 times.
# The range function defines how many iterations take place, in this case starting at 0 up to but not including numberOfNumbers, so 10 times.
for n in range(0, numberOfNumbers):
    # The random.randint() function randomly generates a random integer between 0 and rangeTo.
    # The .append() function adds the randomly generated integer to the queue list. 
    queue.append(random.randint(0, rangeTo))

# The full queue of numbers is printed.
print("The queue is {}".format(queue))

# A while loop executes while the length of the list queue is not zero.
while len(queue) != 0:
    # The integer at index position 0 of the queue list (the first item in the list) is removed from the list using the .pop() function and assigned to the variable "currentNumber".
    # Because the length of the queue has been reduced, the length will eventually become zero enabling the while loop to terminate.
    currentNumber = queue.pop(0)
    # The number that was just removed from the list and the queue after it has been removed are both printed.
    # Because this print statement is within the while loop, it executes at every iteration.
    print("The current number at the top of the queue is {} and the queue is currently {}".format(currentNumber, queue))

# Now that the list is empty, a message is displayed imforming the user that the queue is empty.  
print("The queue is now empty :(")