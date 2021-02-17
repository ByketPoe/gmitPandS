# 8And9xtra.py
# The purpose of this program is to show off ;)
# author: Emma Farrell

# 8.
# 100 is an invalid variable name because it starts with a number. Variables can contain numbers but cannot start with them
# eggs is a valid variable name because it starts with a letter

# 9.
# The functions that can be used to get the integer, floating point number and string versions of a value are demonstrated below.
# The data in the variable "value" is of type float.
value = 3.5
intValue = int(value) # It is converted to an integer.
floatValue = float(intValue) # The integer is converted to a float. The value has been rounded from 3.5 to 3.0 in the previous line.
stringValue = str(value) # The value is converted to a string. 

print(value, type(value), intValue, type(intValue), floatValue, type(floatValue), stringValue, type(stringValue))