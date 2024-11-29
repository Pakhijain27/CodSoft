# Initialize an empty dictionary to store contacts
contacts = {}  
def add_contact():
  name = input("Enter contact name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email address: ")
  address = input("Enter address: ")
  contacts[name] = {"phone": phone, "email": email, "address": address}
  print(f"Contact '{name}' added successfully.")  
def view_contacts():
  if contacts:
    print("Contact List:")
    for name, details in contacts.items():
      print(f"{name}: {details['phone']}")
  else:
    print("No contacts found.")
def update_contact():
  name = input("Enter contact name to update: ")
  if name in contacts:
    phone = input("Enter new phone number: ")
    email = input("Enter new email address: ")
    address = input("Enter new address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' updated successfully.")
  else:
    print("Contact not found.")
def delete_contact():
  name = input("Enter contact name to delete: ")
  if name in contacts:
    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")
  else:
    print("Contact not found.")
# Define the function that was missing in the original code
def search_contact(): #Define the function that was missing in the original code
  name = input("Enter the name of the contact to search for: ")
  if name in contacts:
    print(f"Contact found: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")
    print(f"Address: {contacts[name]['address']}")
  else:
    print(f"Contact '{name}' not found.")
while True:
  print("\nContact Book Menu:")
  print("1. Add Contact")
  print("2. View Contacts")
  print("3. Search Contact")
  print("4. Update Contact")
  print("5. Delete Contact")
  print("6. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    add_contact()
  elif choice == '2':
    view_contacts()
  elif choice == '3':
    search_contact()
  elif choice == '4':
    update_contact()
  elif choice == '5':
    delete_contact()
  elif choice == '6':
    break
  else:
    print("Invalid choice. Please try again.")
