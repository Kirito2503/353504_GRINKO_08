def validate_input(func):
    def wrapper():
        while True:
            try:
                return func()
            except ValueError:
                print("Ошибка: введите целое число!")
    return wrapper

@validate_input
def sum_every_second():
    """
    Задание 2.
    Цикл суммирует каждое второе число, ввод завершается при 0.
    """
    numbers = []
    print("Вводите целые числа (0 для завершения):")
    while True:
        num = int(input("> "))
        if num == 0:
            break
        numbers.append(num)
    
    total = sum(numbers[1::2])  # Сумма каждых вторых элементов
    return total