from contacts import Contact

class AddressBook:
    def __init__(self, name, filename="address_book.txt"):
        self.name = name
        self.contacts = {}
        self.filename = filename
        self.load_from_file()  # Load contacts when initializing

    def save_to_file(self):
        """Saves all contacts to a text file."""
        with open(self.filename, "w") as file:
            for contact in self.contacts.values():
                file.write(f"{contact.first_name},{contact.last_name},{contact.address},"
                           f"{contact.city},{contact.state},{contact.zip_code},"
                           f"{contact.phone_number},{contact.email}\n")
        print(f"\nContacts saved to '{self.filename}'.")

    def load_from_file(self):
        """Loads contacts from a text file into the address book."""
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 8:
                        contact = Contact(*data)
                        self.contacts[contact.full_name] = contact
            print(f"\nContacts loaded from '{self.filename}'.")
        except FileNotFoundError:
            print("\nNo saved contacts found. Starting fresh.")


    def add_contact(self,  contact):
        """Adds a new contact to the address book using full name as a unique key."""
        # Check if the contact already exists
        if contact.full_name in self.contacts:
            print(f"\n{contact.full_name} is already in '{self.name}' Address Book.")

        else:
            self.contacts[contact.full_name] = contact  # Store contact object
            print(f"\nContact '{contact.full_name}' added successfully!")

        #removing duplicates
        for existing_contact  in self.contacts.values():
            if existing_contact  ==  contact.full_name:
                print(f"\n{contact.full_name} is already in '{self.name}' Address Book.")
                break

    def sort_contacts_by_name(self):
        """Sorts contacts alphabetically by full name and displays them."""
        sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.full_name)

        if not sorted_contacts:
            print("\nNo contacts to display.")
            return

        print("\nContacts Sorted by Name:")
        for contact in sorted_contacts:
            print(f"{contact.first_name} {contact.last_name}\n"
                  f"{contact.address}\n"
                  f"{contact.city}, {contact.state} {contact.zip_code}\n"
                  f"{contact.phone_number}\n"
                  f"{contact.email}\n")
        print(f"\n{'-' * 30}")

    def sort_contacts_by_city_zip_state(self, choice):
        """sorts contacts by city , zip code , state"""
        if not self.contacts:
            print("\nNo contacts to display.")
            return
        if choice == "1":
            sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.city)

        elif choice == "2":
            sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.zip_code)

        elif choice == "3":
            sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.state)

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")
            return

        for contact in sorted_contacts:
            print(f"{contact.first_name} {contact.last_name}\n"
                  f"{contact.address}\n"
                  f"{contact.city}, {contact.state} {contact.zip_code}\n"
                  f"{contact.phone_number}\n"
                  f"{contact.email}\n")
            print(f"\n{'-' * 30}")


    def  display_contacts(self):
        if not self.contacts:
            print("\nNo contacts to display.")
            return

        print(f"\nContacts in {self.name} Address Book:")
        for contact in self.contacts.values():
            contact_info = vars(contact)
            for key , value in contact_info.items():
                print(f"{key}: {value}")
            print(f"\n{'-' * 30}")

    def edit_contact(self , full_name):
        """Edit an existing contact using full name as a unique key."""

        if full_name not in self.contacts:
            print(f"\nContact '{full_name}' not found!")
            return

        contact = self.contacts[full_name]
        print(f"\nEditing Contact: {full_name}")

        # Ask for new details; keep old values if left blank
        contact.first_name = input(f"New First Name ({contact.first_name}): ") or contact.first_name
        contact.last_name = input(f"New Last Name ({contact.last_name}): ") or contact.last_name
        contact.address = input(f"New Address ({contact.address}): ") or contact.address
        contact.city = input(f"New City ({contact.city}): ") or contact.city
        contact.state = input(f"New State ({contact.state}): ") or contact.state
        contact.zip_code = input(f"New Zip Code ({contact.zip_code}): ") or contact.zip_code
        contact.phone_number = input(f"New Phone Number ({contact.phone_number}): ") or contact.phone_number
        contact.email = input(f"New Email ({contact.email}): ") or contact.email

        # Update dictionary key if name changes
        new_full_name = contact.full_name  # Uses the updated property
        if new_full_name != full_name:
            self.contacts[new_full_name] = self.contacts.pop(full_name)

        print(f"\nContact '{new_full_name}' updated successfully!")

    def delete_contact(self , full_name):
        """Delete an existing contact using full name as a unique key."""
        if full_name not in self.contacts:
            print(f"\nContact '{full_name}' not found!")
            return

        del self.contacts[full_name]
        print(f"\nContact '{full_name}' deleted successfully!")
