# grade.py
# The purpose of this program is to provide a grade based on the input percentage. 
# It allows for rounding up of grades if the student is 0.5% away from a higher grade bracket.
# author: Emma Farrell

# The percentage is requested from the user and converted to a float. 
# Float is appropriate in this occasion as we do not want people to fail based on rounding to an integer.
percentage = float(input("Enter the percentage: "))

# In this modification of the program, the percentage inputted by the user is rounded.
# As we want to round up if the first decimal place is 0.5 or greater, we do not need to state number of decimal places.
percentageRounded = round(percentage)

# The if statements are executed as in the original program, but evaluating the new variable "percentageRounded" instead of "percentage"
if percentageRounded < 0 or percentageRounded > 100:
    print("Please enter a number between 0 and 100")
elif percentageRounded < 40:
    print("Fail")
elif percentageRounded < 50:
    print("Pass")
elif percentageRounded < 60:
    print("Merit 1")
elif percentageRounded < 70:
    print("Merit 2")
else:
    print("Distinction")