import json 
filename = "testdisct.json"
sample = dict(name = 'fred', age = 31, grades = [1, 34, 55])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj, f)

writeDict(sample)