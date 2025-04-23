def input_list():
    """
    Ввод списка с проверкой данных.
    """
    lst = []
    print("Введите элементы списка (числа):")
    while True:
        try:
            num = float(input("> "))
            lst.append(num)
        except ValueError:
            print("Ошибка: введите число!")
        except KeyboardInterrupt:
            break
    return lst

def repeat_program(func):
    """
    Декоратор для повторного выполнения программы.
    """
    def wrapper():
        while True:
            func()
            if input("Повторить? (y/n): ").lower() != 'y':
                break
    return wrapper