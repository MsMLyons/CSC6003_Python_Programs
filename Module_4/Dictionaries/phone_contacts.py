# Phonebook Contacts
# Create a phonebook dictionary to store contacts with their respective phone numbers.
# Implement the following functionalities:
    # Add a contact to the phonebook.
    # Retrieve the phone number of a given contact.
    # Print all contacts in the phonebook

# initialize dictionary
phonebook = {}

# add a contact to the phonebook
def add_contact(name, phone_number):
    phonebook[name] = phone_number

# retrieve phone number of contact
def get_phone_number(name):
    return phonebook.get(name)

# print all contacts in the phonebook
def print_phonebook():
    for name, phone_number in phonebook.items():
        print(name, ":", phone_number)

# usage
add_contact("Alicia Smith", "123456789")
add_contact("Alex Trebek", "98765432d1")
print(get_phone_number("Alicia Smith"))
print_phonebook()

# output -->
    # 123456789
    # Alicia Smith : 123456789
    # Alex Trebek : 98765432d1