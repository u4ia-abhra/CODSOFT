list = {}
while True:
    while True:
        n = int(input('''Enter 1 to create task
Enter 2 to update task
Enter 3 to view tasks
Enter 4 to delete task
Enter 0 to exit
'''))
        if n == 1 or n == 2 or n == 3 or n==0:
            break
        else:
            print("Invalid Input")

    if n == 1:
        print("You have chosen to create a task")
        name = input("Enter task name: ")
        details = input("Enter task details: ")
        list[name] = details

    if n == 2:
        print("You have chosen to update a task")
        name = input("Enter task name: ")
        if name in list:
            details = input("Enter task details: ")
            list[name] = details
        else:
            print("Entry not present")

    if n == 3:
        print("You have chosen to view tasks")
        print(list.items())

    if n == 4:
        print("You have chosen to delete a task")
        name = input("Enter task name: ")
        if name in list:
            del list[name]
        else:
            print("Entry not present")

    if n == 0:
        break