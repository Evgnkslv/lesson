def bank(X, Y):
    deposit = X
    interest_rate = 0.10  # ставка 10% годовых
    for _ in range(Y):
        deposit += deposit * interest_rate
    return deposit

# Пример-шпаргалка использования функции
X = 1000  # это начальная сумма вклада
Y = 5     # а это количество лет
final_amount = bank(X, Y)
print(f"Сумма на счету после {Y} лет составит: {final_amount:.2f} рублей")