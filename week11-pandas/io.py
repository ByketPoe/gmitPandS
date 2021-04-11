import pandas as pd

listData = {
    'John' :    ['Maths', 23],
    'Jane' :    ['Geography', 66],
    'Mary' :    ['Art', 56],
    'Joseph' :  ['Programming', 27],
    'Kate' :    ['History', 76],
    'Roisin' :  ['Economics', 64],
    'Jill' :    ['Humanities', 83],
    'Josepha' : ['PE', 45],

}

df = pd.DataFrame.from_dict(listData, orient='index', columns = ['Subject', 'Grade']) #
df.index.name = 'Name'
print(df)
print(df.describe())
print(type(df.describe()))