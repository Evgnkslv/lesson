def filter_elements(lst):
    result = [num for num in lst if num < 30 and num % 3 == 0]
    return result

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

filtered_elements = filter_elements(lst)
print("Элементы списка, которые одновременно меньше 30 и делятся на 3 без остатка:")
print(filtered_elements)
