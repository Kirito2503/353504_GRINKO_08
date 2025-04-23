import math

def validate_input(func):
    """Декоратор для обработки некорректного ввода."""
    def wrapper():
        while True:
            try:
                return func()
            except ValueError:
                print("Ошибка: введите корректное число!")
            except Exception as e:
                print(f"Ошибка: {e}")
    return wrapper

@validate_input
def calculate_series():
    """
    Задание 1.
    Вычисление ln(1+x) с помощью степенного ряда.
    """
    x = float(input("Введите x (|x| < 1): "))
    if abs(x) >= 1:
        raise ValueError("|x| должен быть меньше 1!")
    
    eps = float(input("Введите точность eps (например, 0.0001): "))
    if eps <= 0:
        raise ValueError("eps должен быть положительным!")

    term = x          # Первый член ряда
    total = term       # Текущая сумма
    n = 1             # Счетчик итераций
    math_value = math.log(1 + x)

    # Вычисление суммы ряда
    while abs(math_value - total) > eps and n < 500:
        n += 1
        term *= -x * (n - 1) / n
        total += term

    # Вывод результатов
    print(f"x = {x}")
    print(f"F(x) = {total:.6f}")
    print(f"n = {n}")
    print(f"Math F(x) = {math_value:.6f}")

    return total

if __name__ == "__main__":
    calculate_series()