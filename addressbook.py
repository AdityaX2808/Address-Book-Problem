from contacts import Contact

class AddressBookMain:
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