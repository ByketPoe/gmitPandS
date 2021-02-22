# courses.py
# The purpose of this program is to 
# author: Emma Farrell

# A dictionary is defined and assigned to the variable "student".
# The dictionary is comprised of two key value pairs that define the information of the student.
# The first key value pair defines the name of the student.
# The second key value pair defines the modules taken by the student.
# The value is comprised of a list containing two dictionaries.
# Both dictionaries have two entries, the first storing the name of the module, the second storing the grade that the student has in that module.
student = {"name":"Mary",
            "modules": [
                {
                    "courseName": "Programming",
                    "grade": 45
                },
                {
                    "courseName":"History",
                    "grade": 99
                }

            ]
        }

# A print statement prints the student's name from the dictionary using the key "name" to access the value. 
print("Student: {}".format(student["name"]))

# A for loop iterates through each item in the modules list.
# The key "modules" is used to access the list, which is the value assigend to that key within the dictionary "student".
for module in student["modules"]:
    # For each item in the list, the name of the module and the grade the student earned for that module is printed.
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))