def displayMenu():
    print("What would you like to do?\n\t(a) Add a new student\n\t(v) View students\n\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip().lower() # convert to lowercase?

    return choice

def doAdd():
    # do stuff
    print("In Adding")

def doView():
    # do stuff
    print("In Viewing")

# Main Program
choice = displayMenu()
while (choice != "q"):
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print("\n\nPlease select either a, v, or q")
    print("You chose {}".format(choice))
    choice = displayMenu()
    
print("You chose {}".format(choice))