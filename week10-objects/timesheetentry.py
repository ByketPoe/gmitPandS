# timesheetentry.py
# The purpose of this program is to enter data into time sheets. 
# author: Emma Farrell

import datetime as dt

class Timesheetentry:

    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration

    def __str__(self):
        return self.project +':'+ str(self.duration)

if __name__ == '__main__':
    ts = dt.datetime(2021,3,19,16,20)
    test = Timesheetentry('test', ts, 60)
    print(test)

