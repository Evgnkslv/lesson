from smartphone import Smartphone

# Создаем список для хранения экземпляров класса Smartphone
catalog = []

# Создаем пять разных экземпляров для класса Smartphone
phone1 = Smartphone("Apple", "iPhone 15", "+79855655777")
phone2 = Smartphone("Samsung", "Galaxy S24", "+79009000909")
phone3 = Smartphone("Xiaomi", "Redmi Note 12", "+79011001010")
phone4 = Smartphone("OnePlus", "10 Pro", "+79876543210")
phone5 = Smartphone("Google", "Pixel 9", "+79123456789")

# Добавляем созданные экземпляры в список catalog
catalog.extend([phone1, phone2, phone3, phone4, phone5])

# Выводим каталог телефонов
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")