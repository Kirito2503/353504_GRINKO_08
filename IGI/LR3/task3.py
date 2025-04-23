def count_digits(text: str) -> int:
    """
    Задание 3.
    Подсчет количества цифр в строке без использования регулярных выражений.
    """
    return sum(1 for char in text if char.isdigit())