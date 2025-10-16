def print_list_semicolon(my_list):
    """
    Принимает список и выводит его элементы в консоль,
    разделяя их точкой с запятой.

    Args:
        my_list (list): Список для вывода.
    """
    print(*my_list, sep=';')

# --- Примеры использования функции ---

list1 = [1, 2, 3, 4, 5]
print("Пример 1:")
print_list_semicolon(list1)
# Ожидаемый вывод: 1;2;3;4;5

list2 = ['apple', 'banana', 'cherry']
print("\nПример 2:")
print_list_semicolon(list2)
# Ожидаемый вывод: apple;banana;cherry

list3 = []
print("\nПример 3 (пустой список):")
print_list_semicolon(list3)
# Ожидаемый вывод: (пустая строка, так как элементов нет)

