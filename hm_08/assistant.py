import pickle
from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
            self.date = parsed_date
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def change_phone(self, old: str, new: str):
        for i, phone in enumerate(self.phones):
            if phone.value == old:
                self.phones[i] = Phone(new)
                return True
        return False

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.now().date()
        bday = self.birthday.date.replace(year=today.year)
        if bday < today:
            bday = bday.replace(year=today.year + 1)
        return (bday - today).days


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        result = []

        for record in self.data.values():
            if not record.birthday:
                continue

            bday = record.birthday.date.replace(year=today.year)
            if bday < today:
                bday = bday.replace(year=today.year + 1)

            if today <= bday <= next_week:
                result.append(
                    {
                        "name": record.name.value,
                        "birthday": record.birthday.date.strftime("%d.%m.%Y"),
                        "in_days": (bday - today).days,
                    }
                )

        return sorted(result, key=lambda x: x["in_days"])


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Not enough arguments provided."
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.data.get(name)
    message = "Contact updated."
    if not record:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old, new, *_ = args
    record = book.data.get(name)
    if not record:
        raise KeyError()
    if record.change_phone(old, new):
        return "Phone updated."
    else:
        return "Old phone not found."


@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    record = book.data.get(name)
    if not record:
        raise KeyError()
    return f"{name}: {', '.join(p.value for p in record.phones)}"


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.data.get(name)
    if not record:
        raise KeyError()
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.data.get(name)
    if not record:
        raise KeyError()
    if not record.birthday:
        return "Birthday not set."
    return f"{name}'s birthday: {record.birthday.value}"


@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    return "\n".join(
        f"{u['name']}: {u['birthday']} (in {u['in_days']} days)" for u in upcoming
    )


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "No contacts available."
    result = []
    for name, record in book.data.items():
        phones = ", ".join(phone.value for phone in record.phones)
        bday = f", Birthday: {record.birthday.value}" if record.birthday else ""
        result.append(f"{name}: {phones}{bday}")
    return "\n".join(result)


def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    book = load_data()  # ← Завантаження з файлу
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)  # ← Збереження перед виходом
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phones(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
