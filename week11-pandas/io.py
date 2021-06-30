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

path = "./data/" # need to create the directory first, df.to_csv creates files but not directories
csvFilename = path + "grades.csv"
df.to_csv(csvFilename)

excelFilename = path + "grades.xlsx"
df.to_excel(excelFilename, index=False, sheet_name="data") # index=False removes index column

with pd.ExcelWriter(excelFilename, engine="openpyxl", mode="a") as writer:
    df.describe().to_excel(writer, sheet_name="summary")

# mean = df.describe().loc["mean", "Grade"]
mean = df["Grade"].mean()
print(mean)
