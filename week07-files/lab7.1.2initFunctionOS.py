# Part a
filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

# Part b
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

# Discussion: init function
def init():
    print("file does not exist")
    writeNumber(0)

# Discussion: check using os module
import os.path
if not os.path.isfile(filename):
    init()

# Part c
num = readNumber()
num += 1
print("We have run this program {} times".format(num))
writeNumber(num)