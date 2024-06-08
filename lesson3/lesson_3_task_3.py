from address import Address
from mailing import Mailing

# Создание адреса
to_address = Address("140400", "Коломна", "Гажданская улица", "106", "1")
from_address = Address("140400", "Коломна", "Гранатная улица", "1", "1")

# Создаем отправление
mailing = Mailing(to_address, from_address, 500, "RC123456789RU")

# Выводим информацию об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")