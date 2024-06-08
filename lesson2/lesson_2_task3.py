import math

def square(side):
    area = side ** 2
    if not isinstance(area, int):
        area = math.ceil(area)
    return area

# Проверка функции для стороны квадрата равной 5 ну или можно любое число
side_length = 5
result = square(side_length)

print(f"Площадь квадрата с стороной {side_length} = {result}")