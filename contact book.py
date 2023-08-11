import time

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    name = name.lower()  
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print("Adding contact")
    time.sleep(2)
    print("Contact added successfully!")

def search_contact():
    name = input("Enter contact name to search: ")
    name = name.lower()  
    if name in contacts:
        contact = contacts[name]
        print("Contact Details:")
        print("Name:", name.capitalize())  
        print("Phone:", contact["Phone"])
        print("Email:", contact["Email"])
    else:
        print("Contact not found!")

def delete_contact(): 
    name = input("Enter contact name to delete:")
    if name in contacts:
        del contacts[name]
        print("Deleting contact")
        time.sleep(2)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if contacts:
        print("Contacts List:")
        for name, contact in contacts.items():
            print("<---------------------------------------------------->")
            print("Name:", name.capitalize())
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("<---------------------------------------------------->")
    else:
        print("Contact list is empty")

def main():
    while True:
        print("\n------- Contact Book -------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")                      
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Closing Contact Book")
            time.sleep(2)
            print("Contact book closed")
            break
        else:
            print("Invalid choice. Please try again.")


main()
