def displayMenu():
    print("What would you like to do?\n\t(a) Add a new student\n\t(v) View students\n\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip().lower() # convert to lowercase?

    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter the next module name (blank to quit): ").strip()

    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

def doNothing(dummyVariable):
    pass

choiceMap = {'a': doAdd, 'v': doView, 'q': doNothing}

# Main Program
student_list = []
choice = displayMenu()
while choice != "q":
    if choice in choiceMap:
        choiceMap[choice](student_list)
    else:
        print("\n\nPlease select either a, v, or q")
    print("You chose {}".format(choice))
    choice = displayMenu()
    
print("You chose {}".format(choice))
print(student_list)