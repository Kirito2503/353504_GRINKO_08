def process_list(lst: list):
    """
    Задание 5.
    Обработка списка: номер макс. по модулю, произведение между нулями.
    """
    # Номер максимального по модулю
    max_abs_idx = max(range(len(lst)), key=lambda i: abs(lst[i]))
    print(f"Номер максимального по модулю элемента: {max_abs_idx + 1}")

    # Индексы первого и второго нулей
    zeros = [i for i, x in enumerate(lst) if x == 0]
    if len(zeros) < 2:
        print("Недостаточно нулей для вычисления произведения.")
        return

    start, end = zeros[0], zeros[1]
    product = 1
    for num in lst[start+1:end]:
        product *= num
    print(f"Произведение между первым и вторым нулями: {product}")