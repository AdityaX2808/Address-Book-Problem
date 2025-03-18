from contacts import Contact

class AddressBook:
    def __init__(self, name):
        self.contacts = {}
        self.name = name

    def add_contact(self, contact):
        """Adds a new contact to the address book using full name as a unique key."""
        full_name = contact.full_name.title()

        if full_name in self.contacts:
            print(f"\n{full_name} is already in '{self.name}' Address Book.")
        else:
            self.contacts[full_name] = contact
            print(f"\nContact '{full_name}' added successfully!")

    def display_contacts(self):
        """Displays all contacts in the address book."""
        if not self.contacts:
            print("\nNo contacts to display.")
        else:
            print(f"\nContacts in '{self.name}' Address Book:")
            for contact in self.contacts.values():
                print(f"\nFull Name: {contact.full_name.title()}")
                print(f"Address: {contact.address.capitalize()}")
                print(f"City: {contact.city.capitalize()}")
                print(f"State: {contact.state.capitalize()}")
                print(f"Zip Code: {contact.zip_code}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("-" * 30)

    def edit_contact(self , full_name):
        """Edit an existing contact using full name as a unique key."""
        full_name = full_name.title()

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

        print(f"\nContact '{full_name}' updated successfully!")

        # Update the key in the dictionary if the full name has changed
        new_full_name = contact.full_name.title()
        if new_full_name != full_name:
            self.contacts[new_full_name] = self.contacts.pop(full_name)