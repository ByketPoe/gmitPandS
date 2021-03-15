def displayMenu():
    print("What would you like to do?\n\t(a) Add a new student\n\t(v) View students\n\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip() # convert to lowercase?

    return choice

choice = displayMenu()
print("You chose {}".format(choice))