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