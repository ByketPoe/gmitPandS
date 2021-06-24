# employee.py
# The purpose of this program is to define employees. 
# author: Emma Farrell

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first +' '+ self.last

if __name__ == '__main__':
    test = Employee('Joe', 'Bloggs')
    print(test)
    assert ('some one' == str(test))