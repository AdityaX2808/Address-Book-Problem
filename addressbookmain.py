from addressbook import AddressBook


class AddressBookMain:
    """this class is used to create and manage multiple address books"""
    def __init__(self):
        self.addressbook = {}

    def add_address_book(self ,name):
        """this function creates a new address book"""
        if name in self.addressbook.keys():
            print(f"\n'{name}' Address Book already exists.")
        else:
            self.addressbook[name] = AddressBook(name)
            print(f"\n'{name}' Address Book created successfully!")

    def display_address_books(self):
        """this function displays all the address books"""
        if not self.addressbook:
            print("\nNo Address Books to display.")
        else:
            print(f"\nAddress Books:")
            for name in self.addressbook.keys():
                print(f"\n{name}")

    def select_address_book(self , name):
        """this method selects the address book to work with"""
        if name in self.addressbook:
            return self.addressbook[name]
        print(f"\n'{name}' Address Book not found!")
        return None

    def delete_address_book(self , name):
        """this method deletes the address book"""
        if name in self.addressbook:
            del self.addressbook[name]
            print(f"\n'{name}' Address Book deleted successfully!")
        else:
            print(f"\n'{name}' Address Book not found!")

#create class to search person on the basis of city or state
class SearchPerson(AddressBookMain):
    def search_person(self, city):
        """this function searches a person in all address books by city or state"""
        found = False
        for address_book in self.addressbook.values():
            for contact in address_book.contacts.values():
                if city == contact.city:
                    print(f"\nContact found in '{address_book.name}' Address Book:")
                    contact_info = vars(contact)
                    for key, value in contact_info.items():
                        print(f"{key}: {value}")
                    print(f"\n {'-' * 30}")
                    found = True
        if not found:
            print("\nContact not found in any Address Book.")