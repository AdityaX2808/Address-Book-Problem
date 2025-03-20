from addressbookmain import AddressBookMain , SearchPerson
from addressbook import AddressBook
from contacts import Contact
from validation import (
    validate_first_name, validate_last_name, validate_address,
    validate_city, validate_state, validate_zip_code,
    validate_phone_number, validate_email
)


def main():
    print("\nWelcome to the Address Book System!")

    Mainbook = AddressBookMain()

    while True:
        print("\nOptions: ")
        print("1. Create Address Book")
        print("2. Select Address Books")
        print("3. Display Address Book")
        print("4. Delete Address Book")
        print("5. Search Contact Using City")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
           name = input("Enter new Address Book name: ").strip()
           Mainbook.add_address_book(name)

        elif choice == "2":
            name = input("Enter the  Address Book to select: ").strip()
            book = Mainbook.select_address_book(name)

            if book:
                manage_contact(book)

        elif choice == "3":
            Mainbook.display_address_books()

        elif choice  == "4":
            name = input("Enter the Address Book to delete: ").strip()
            Mainbook.delete_address_book(name)

        elif choice == "5":
            city = input("Enter the city name to search contacts: ").strip()
            Mainbook = SearchPerson(city , Mainbook)
            Mainbook.search_person()

        elif choice =="6":
            exit("\nExiting the program, Goodbye!!!.....")

def  manage_contact(book):
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Sort by name")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            # Validate and take all inputs
            first_name = validate_first_name("Enter First Name: ").strip()
            last_name = validate_last_name("Enter Last Name: ").strip()
            address = validate_address("Enter Address: ")
            city = validate_city("Enter City: ")
            state = validate_state("Enter State: ")
            zip_code = validate_zip_code("Enter Zip Code: ")
            phone_number = validate_phone_number("Enter Phone Number: ")
            email = validate_email("Enter Email: ")

            # Create a new contact and add to address book
            contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            book.add_contact(contact)

        elif choice == "2":
            book.display_contacts()

        elif choice == "3":
            book.edit_contact(input("Enter the full name of the contact you want to edit: ").strip().title())

        elif choice == "4":
            book.delete_contact(input("Enter the full name of the contact you want to delete: ").strip().title())

        elif choice == "5":
            book.sort_contacts_by_name()

        elif choice == "6":
            break

if __name__ == "__main__":
    main()


