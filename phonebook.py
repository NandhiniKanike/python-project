
contacts={}
print("Welcome to Phone Book Application")
menu = {
    1: "Add a New Contact",
    2: "Search for a Contact",
    3: "Delete a contact",
    4: "List all contacts"
}
while True:
    print("\nMenu:")
    print("1.Add a New Contact\n","2.Search for a Contact\n","3.Delete a contact\n","4.List all contacts")
    user=int(input("Enter your choice:"))
    if user in menu:
        if user == 1:
            name = input("Enter the name of the contact: ")
            if name in contacts:
                print("Contact already present")
            else:
                phonenumber = input("Enter the phone number of the contact: ")
                if len(phonenumber) == 10 and phonenumber.isdigit():
                    contacts[name] = phonenumber
                    print("Contact added successfully")
                else:
                    print("Invalid phone number. Please enter a 10-digit number.")
        elif user==2:
            name=input("Enter the name of the contact you want to search:")
            if name in contacts:
                print(f"The phone number of the contact {name} is {contacts[name]}")
            else:
                print("Contact is not present")
        elif user==3:
            name=input("Enter the name you want to delete:")
            if name in contacts:
                del contacts[name]
                print("Contact is deleted successfully")
            else:
                print("Contact is not present to delete")
        elif user==4:
            if contacts=={}:
                print("No contacts available")
            else :
                for name,phonenumber in contacts.items():
                    print(f"Name:{name},Phone Number:{phonenumber}")
    else:
            print("Invalid option,Enter the correct option!!!")
    cont=input("Do you wan to continue(Yes/No):")
    if cont.lower() == "yes":
        continue
    elif cont.lower()== "no":
        print("Thank you for using Phone Book Application")
        break
    else:
        print("Invalid input. Exiting the application.")
        break