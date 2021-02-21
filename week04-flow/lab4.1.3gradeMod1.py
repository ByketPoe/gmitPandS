# gradeMod1.py
# The purpose of this program is to provide a grade based on the input percentage. 
# It allows for rounding up of grades if the student is 0.5% away from a higher grade bracket.
# author: Emma Farrell

# The percentage is requested from the user and converted to a float. 
# Float is appropriate in this occasion as we do not want people to fail based on rounding to an integer.
percentage = float(input("Enter the percentage: "))

# In this modification of the program, the numbers that define the grade brackets are altered to account for grades that fall within 0.5% 
if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 39.5:
    print("Fail")
elif percentage < 49.5:
    print("Pass")
elif percentage < 59.5:
    print("Merit 1")
elif percentage < 69.5:
    print("Merit 2")
else:
    print("Distinction")