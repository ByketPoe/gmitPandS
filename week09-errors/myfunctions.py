# myfunctions.py
# The purpose of this program is to create a Fibonacci sequence based on user input. 
# author: Emma Farrell

import logging
# logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number == 0:
        return[]
    if number < 0:
        raise ValueError('number must be > 0')
    a = 0
    b = 1
    fibonacciSequence = [0]
    for i in range(1, number):
        fibonacciSequence.append(b)
        a, b = b, a + b
    logging.debug("%d: %s", number, fibonacciSequence)
    return fibonacciSequence


if __name__ == '__main__':
    print("all good")

return7 = [0, 1, 1, 2, 3, 5, 8]
return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return for 0'
assert fibonacci(1) == [0],'incorrect return for 1'

try:
    fibonacci(-1)
except ValueError:
    pass
else:
    assert False, 'fibonacci missing ValueError'