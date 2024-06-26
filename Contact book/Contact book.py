book = {"Me":["Abhrajit Ghosh",9051068685,"abhrajitgh@gmail.com","Kolkata"]}

while True:
    while True:
        choice = int(input('''Enter 1 to Add Contact
Enter 2 to View Contact List
Enter 3 to Search Contact
Enter 4 to Update Contact
Enter 5 to Delete Contact
Enter 0 to Exit
'''))
        if choice == 0 or choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
            break
        else:
            print("Invalid Input")

    if choice == 1:
        print("You have selected to add contact")
        name = input("Enter name: ")
        number = int(input("Enter phone number: "))
        email = input("Enter email: ")
        address = input("Enter address: ")
        book[name] = [name, number, email, address]

    if choice == 2:
        print("You have selected to view contact list")
        l = book.items()
        for i in l:
            print(i)

    if choice == 3:
        print("You have selected to search contact")
        name: str = input("Enter contact name: ")
        print("Name: ", book[name][0])
        print("Number: ", book[name][1])
        print("Email: ", book[name][2])
        print("Address: ", book[name][3])

    if choice == 4:
        print("You have selected to update contact")
        name = input("Enter name: ")
        number = int(input("Enter phone number: "))
        email = input("Enter email")
        address = input("Enter address")
        book[name] = [name, number, email, address]

    if choice == 5:
        print("You have selected to delete contact")
        name: str = input("Enter contact name: ")
        del book[name]

    if choice == 0:
        break
