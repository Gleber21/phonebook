class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Контакт не найден.")

    def find_contact(self, name):
        return self.contacts.get(name, "Контакт не найден.")

    def list_all_contacts(self):
        for name, phone_number in self.contacts.items():
            print(f"{name}: {phone_number}")

# Пример использования
phone_book = PhoneBook()
phone_book.add_contact("Иван Иванов", "123-456-789")
phone_book.add_contact("Петр Петров", "987-654-321")
print(phone_book.find_contact("Иван Иванов"))
phone_book.list_all_contacts()
phone_book.remove_contact("Иван Иванов")
