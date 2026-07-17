import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    contacts = load_contacts()

    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("\n✅ Contact added successfully.\n")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n===== CONTACT LIST =====")

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")

    print()


def search_contact():
    contacts = load_contacts()

    name = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if name in contact["name"].lower():
            print("\nContact Found")
            print("----------------")
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("\nContact not found.\n")


def update_contact():
    contacts = load_contacts()

    name = input("Enter contact name to update: ").lower()

    for contact in contacts:

        if contact["name"].lower() == name:

            new_phone = input(f"New Phone ({contact['phone']}): ").strip()
            new_email = input(f"New Email ({contact['email']}): ").strip()

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)

            print("\n✅ Contact updated.\n")
            return

    print("\nContact not found.\n")


def delete_contact():
    contacts = load_contacts()

    name = input("Enter contact name to delete: ").lower()

    for contact in contacts:

        if contact["name"].lower() == name:

            contacts.remove(contact)
            save_contacts(contacts)

            print("\n🗑 Contact deleted.\n")
            return

    print("\nContact not found.\n")


def menu():

    while True:

        print("======== CONTACT BOOK ========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("\nInvalid choice.\n")


if __name__ == "__main__":
    menu()