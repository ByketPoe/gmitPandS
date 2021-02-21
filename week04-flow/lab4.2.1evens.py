# evens.py
# The purpose of this program is to print all of the numbers from 2 to 100.
# author: Emma Farrell

# The start point, end point and step value are defined and assigned to variables. 
endPoint = 100
startPoint = 2
step = 2

# The while loop evaluates the value of startPoint and checks to see if it is less than or equal to endPoint.
# Initially, the value of startPoint is 2. This increases by 2 every iteration of the loop.
# To print 100, we use <= because if we just used <, 100 would not get printed as the loop would not get executed when startPoint = 100.
while startPoint <= endPoint:
    # The current value of startPoint is printed.
    print(startPoint)
    # The value of startPoint is incremented by the value of step, which is 2. 
    # If this line was not in the loop, it would execute infinitely.
    startPoint += step