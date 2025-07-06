import re
from collections import UserDict
from dataclasses import dataclass, field


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        if not re.fullmatch(r"\d{10}", new_value):
            raise ValueError("Phone number must be 10 digits.")
        self._value = new_value


@dataclass
class Record:
    name: Name
    phones: list[Phone] = field(default_factory=list)

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)

    def edit_phone(self, old_number: str, new_number: str):
        phone = self.find_phone(old_number)
        if phone:
            phone.value = new_number
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone_number: str):
        return next((p for p in self.phones if p.value == phone_number), None)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


@dataclass
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        self.data.pop(name, None)
