from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) < 7:
            raise ValueError("Phone number must be at least 7 digits.")
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
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

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
