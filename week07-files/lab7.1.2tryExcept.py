# Part a
filename = "count.txt"
def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0

# Part b
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

# Part c
num = readNumber()
num += 1
print("We have run this program {} times".format(num))
writeNumber(num)