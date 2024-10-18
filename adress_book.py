from collections import UserDict
from datetime import datetime, timedelta




class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y')
            print(self.value, 'value')
        except Exception as e:
            print(e)   

class Name(Field):
   def __init__(self, name):
       if not name:
           raise ValueError("Name can't be empty")
       self.value = name

class Phone(Field):
    def __init__(self, phone):
        if not phone:
            raise ValueError("Phone can't be empty")
        if len(phone) < 10:
            raise ValueError("Phone must be 10 characters")
        if not phone.isdigit():
            raise ValueError("Phone must be digits")
        self.value = phone

    

    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        print(self, 'self')
        print('Birthday added')

    def show_birthday(self):
        return f"Birthday: {self.birthday.value.strftime('%d.%m.%Y')}"    

    # реалізація класу
    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
             raise ValueError("Phone not found")

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            self.phones.remove(phone)
            self.phones.append(new_phone)
        else:
            print("Phone not found")

    def get_name(self):
        return self.name.value
    
    def get_phones(self):
        return self.phones
    
    def get_birthday(self):
        # return date as a string
        if self.birthday.value:
            return self.birthday.value.strftime('%d.%m.%Y')
        else:
            return None

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        else:
            raise ValueError("Phone not found") 
    def show_phones(self):
        return '; '.join(p.value for p in self.phones)  

    def show_record(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value.strftime('%d.%m.%Y') if self.birthday else 'No birthday'}"             

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value.strftime('%d.%m.%Y') if self.birthday else 'No birthday'}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, Record):
        self.data[Record.name.value] = Record
    
    def find(self, name):
        if name in self.data:
            return self.data[name]
       
            
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")
        
            
    
    from datetime import datetime, timedelta

    def get_upcoming_birthdays(self):
        # Retrieve users from the data attribute
        users = self.data.values()
        
        # Get today's date
        today = datetime.today().date()
        
        # Initialize a list to store upcoming birthdays
        congratulation = []
        
        # Iterate over each user
        for user in users:
            # Skip users without a birthday
            if not user.get_birthday():
                continue
            
            # Parse the user's birthday string into a datetime object
            birthday = datetime.strptime(user.get_birthday(), "%d.%m.%Y").date()
            
            # If the birthday has passed this year, set it to next year
            if birthday < today:
                birthday = birthday.replace(year=today.year)
            
            # Calculate the number of days until the user's birthday
            days_to_birthday = (birthday - today).days
            
            # Adjust the days if the birthday falls on a weekend
            if days_to_birthday <= 7:
                if birthday.weekday() in (5, 6):
                    days_to_birthday += 7 - birthday.weekday()
            
            # If the birthday is within the next 7 days, add it to the congratulation list
            if days_to_birthday <= 7:
                congratulation.append({
                    "name": user.get_name(),
                    "congratulation_date": (today + timedelta(days=days_to_birthday)).strftime("%Y.%m.%d")
                })
        
        # Return the list of upcoming birthdays or a message if there are none
        return congratulation if len(congratulation) > 0 else 'No congratulation'

        

if __name__ == "__main__":
    pass
    # r = Record('John')
    # r.add_phone('123456789')
    # r.add_phone('123456789')
    # r.add_phone('123456789')
    # print(r.show_phones())
    # r.add_birthday('12.12.1980')
    # print(r.show_birthday())
    # book = AddressBook()
    # book.add_record(r)
    # print(book.get_upcoming_birthdays())
    # print(book.data)
    # book.delete('John')
    # print(book.data)

