

def add_contact(contacts):  
    name = input("Enter Name:")
    if name in contacts:
        print("user already exits.")
        return
    phone = input("Enter Phone Number:")
    email = input("Enter Email:")
    contacts[name] = {"phone":phone,"email":email}
    print(" ====== Contact Added. ====== ")


def search_contact(contacts):
    search_name = input("Enter Name: ")
    if search_name in contacts:
        findContact = contacts[search_name]
        print(f"\n* Name: {search_name} Phone: {findContact['phone']} Email: {findContact['email']}")
    else: 
        print("====== Contact not Found ======")


def update_contact(contacts):
    name = input("Enter name to update: ")
    if name not in contacts:
        print("contact not found")
        return
    phone = input("Enter New Phone: ")
    email = input("Enter New Email: ")

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
        print("====== Contact Updated ======")


def view_contacts(contacts):
    if not contacts:
        print(" ====== No Contacts ======")
    else:
        print("====== All Contacts ======")
        for name,contact in contacts.items():
            print(f"\n* Name: {name}, Phone: {contact['phone']}, Email : {contact['email']}")
    



def menu():
    contacts = {}
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. View Contacts")        
        print("5. Exit") 
        
        choice = input("\nEnter choice (1-5): ")       
        
        if choice == '1':
            add_contact(contacts)
        elif choice == "2":
            update_contact(contacts)
        elif choice ==  "3":
            search_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice Try Again\n")    
            
            
if __name__ == '__main__':
    menu()
            