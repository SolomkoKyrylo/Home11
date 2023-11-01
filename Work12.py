import pickle

def save_address_book(address_book, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(address_book, file)

def load_address_book(file_name):
    try:
        with open(file_name, 'rb') as file:
            address_book = pickle.load(file)
        return address_book
    except FileNotFoundError:
        return []

def search_contacts(address_book, search_query):
    found_contacts = []
    for contact in address_book:
        if search_query in contact['name'] or search_query in contact['phone']:
            found_contacts.append(contact)
    return found_contacts


address_book = []

while True:
    print("Меню:")
    print("1. Додати контакт")
    print("2. Пошук контактів")
    print("3. Зберегти адресну книгу")
    print("4. Відновити адресну книгу")
    print("5. Вийти з програми")
    
    choice = input("Виберіть опцію: ")
    
    if choice == '1':
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        address_book.append({'name': name, 'phone': phone})
    
    elif choice == '2':
        search_query = input("Введіть запит для пошуку: ")
        found_contacts = search_contacts(address_book, search_query)
        if found_contacts:
            print("Знайдені контакти:")
            for contact in found_contacts:
                print(f"Ім'я: {contact['name']}, Номер телефону: {contact['phone']}")
        else:
            print("Контакти за запитом не знайдені.")
    
    elif choice == '3':
        file_name = input("Введіть ім'я файлу для збереження: ")
        save_address_book(address_book, file_name)
        print("Адресну книгу збережено в файлі.")
    
    elif choice == '4':
        file_name = input("Введіть ім'я файлу для відновлення: ")
        address_book = load_address_book(file_name)
        print("Адресну книгу відновлено з файлу.")
    
    elif choice == '5':
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
