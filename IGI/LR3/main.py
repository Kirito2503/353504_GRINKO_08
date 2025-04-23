from task1 import calculate_series
from task2 import sum_every_second
from task3 import count_digits
from task4 import analyze_text
from task5 import process_list
from utils import input_list, repeat_program

@repeat_program
def main():
    print("Лабораторная работа №3. Вариант 8. Выполнил Гринко Егор")
    choice = input("Выберите задание (1,2,3,4,5): ")
    
    if choice == "1":
        calculate_series()
    
    elif choice == "2":
        result = sum_every_second()
        print(f"Сумма каждых вторых чисел: {result}")
    
    elif choice == "3":
        text = input("Введите строку: ")
        count = count_digits(text)
        print(f"Количество цифр: {count}")
    
    elif choice == "4":
        analyze_text()
    
    elif choice == "5":
        lst = input_list()
        process_list(lst)
    
    else:
        print("Ошибка: выберите задание из списка.")

if __name__ == "__main__":
    main()