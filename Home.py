from datetime import datetime

class Field:
    def __init__(self, value=None):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    value = property(get_value, set_value)

class Phone(Field):
    def set_value(self, value):
        
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError("Некоректний номер телефону")
        self._value = value

class Birthday(Field):
    def set_value(self, value):
        
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Некоректний формат дня народження. Використовуйте YYYY-MM-DD.")
        self._value = value

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = Field(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today()
            next_birthday = datetime(today.year, int(self.birthday.value[5:7]), int(self.birthday.value[8:10]))
            if today > next_birthday:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_left = (next_birthday - today).days
            return days_left
        else:
            return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        if isinstance(record, Record):
            self.records.append(record)
        else:
            raise ValueError("Додавати можна тільки об'єкти класу Record")

    def iterator(self, batch_size=10):
        for i in range(0, len(self.records), batch_size):
            yield self.records[i:i + batch_size]
