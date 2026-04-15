'''give me a python code for dictionary-based program'''
# A simple dictionary-based program to manage a phone book
class PhoneBook:
    def __init__(self):
        """Initialize the phone book as an empty dictionary."""
        self.contacts = {}

    def add_contact(self, name, phone_number):
        """
        Add a contact to the phone book.

        Parameters:
        name (str): The name of the contact.
        phone_number (str): The phone number of the contact.

        Raises:
        ValueError: If the name or phone number is empty.
        """
        if not name or not phone_number:
            raise ValueError("Name and phone number cannot be empty.")
        self.contacts[name] = phone_number

    def get_contact(self, name):
        """
        Retrieve a contact's phone number by their name.

        Parameters:
        name (str): The name of the contact to retrieve.

        Returns:
        str: The phone number of the contact.

        Raises:
        KeyError: If the contact does not exist in the phone book.
        """
        if name not in self.contacts:
            raise KeyError(f"Contact '{name}' not found in the phone book.")
        return self.contacts[name]

    def delete_contact(self, name):
        """
        Delete a contact from the phone book by their name.

        Parameters:
        name (str): The name of the contact to delete.

        Raises:
        KeyError: If the contact does not exist in the phone book.
        """
        if name not in self.contacts:
            raise KeyError(f"Contact '{name}' not found in the phone book.")
        del self.contacts[name]

    def list_contacts(self):
        """
        List all contacts in the phone book.

        Returns:
        dict: A dictionary of all contacts with names as keys and phone numbers as values.
        """
        return self.contacts
# Example usage
phone_book = PhoneBook()
phone_book.add_contact("Alice", "123-456-7890")
phone_book.add_contact("Bob", "987-654-3210")
print(phone_book.get_contact("Alice"))  # Output: 123-456-7890
print(phone_book.list_contacts())        # Output: {'Alice': '123-456-7890', 'Bob': '987-654-3210'}
phone_book.delete_contact("Bob")
print(phone_book.list_contacts())        # Output: {'Alice': '123-456-7890'}
