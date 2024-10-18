from typing import Callable
from functools import wraps
from adress_book import AddressBook,Record
import pickle

def input_error(func: Callable)-> Callable:

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e)  # Pass other exceptions through

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    if not args:
        raise ValueError('Give me name  please.')
    name,phone= None, None
    if len(args) == 1:
        name = args[0]
    if len(args) == 2:
        name, phone = args    
   
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message



@input_error
def change_contact(args, book:AddressBook):
    name, phone, *_= args
    if not name:
        raise ValueError('Please enter contact name')
    if not phone:
        raise ValueError('Please enter phone')
    record = book.find(name)
    if record:
        record.add_phone(phone)
        book.add_record(name)
        return "Contact changed."


@input_error
def show_contacts(book:AddressBook):
    book = book.data
    for name, record in book.items():
        print(record.show_record())

@input_error
def show_phone(args, book:AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        print(record.show_phones())


@input_error
def add_birthday(args, book:AddressBook):
    name,birthday = args
    if not name :
        raise ValueError ('Please enter name')
    if not birthday:
        raise ValueError ('Please enter birthday')
    record = book.find(name)
    if record:
        record.add_birthday(birthday)

@input_error
def show_birthday(args, book:AddressBook):
    name = args[0]
    record = book.find( name)
    if record:
        print(record.get('birthday'))

    
    

@input_error
def birthdays( book:AddressBook):
    print(book.get_upcoming_birthdays())    


      


def main():
    try:
        with open("address_book.pkl", "rb") as file:

            book = pickle.load(file)
            print('adressbook loaded')
    except FileNotFoundError:
        book = AddressBook({"John": Record("John")})

    add_contact(["John", "12345678910"], book=book)
    add_birthday(["John", "09.03.2000"], book=book)
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            with open("address_book.pkl", "wb") as file:
                pickle.dump(book, file)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book=book))

        elif command == "change":
            print(change_contact(args, book=book))

        elif command == "phone":
            print(show_phone(args, book=book))

        elif command == "all":
            print(show_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book=book))

        elif command == "show-birthday":
            show_birthday(args, book=book)

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

