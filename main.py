from addressbook import AddressBookMain
from contacts import Contact
from validation import (
    validate_first_name, validate_last_name, validate_address,
    validate_city, validate_state, validate_zip_code,
    validate_phone_number, validate_email
)

def main():
    print("\nWelcome to the Address Book System!")

    book = AddressBookMain("Address Book 1")

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Exit")

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
            exit("\nExiting the program, Goodbye!!!.....")

if __name__ == "__main__":
    main()

