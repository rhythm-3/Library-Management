#Module: Library MAnagement

import Menulib
import Book 
import Issue
while True:
    Book.clrscreen()
    print("\t\t\t Library Management\n")
    print("============================================================================")
    print("1. Book Management")
    print("2. Members Management")
    print("3. Issue/Return Book")
    print("4. Exit")
    print("============================================================================")
    choice = int(input("Enter Choice Between 1 to 4 : "))
    if choice == 1:
        Menulib.MenuBook()
    elif choice == 2:
        Menulib.MenuMember()
    elif choice == 3:
        Menulib.MenuIssueReturn()
    elif choice == 4:
        break
    else:
        print("Wrong Choice......Enter Your Choice Again")
        x = input("Press any key to continue")
