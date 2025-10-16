import os

def count_directories(path_list):
    """
    Принимает список путей и возвращает количество путей,
    которые являются директориями.

    Аргументы:
        path_list (list): Список строк, представляющих пути к файлам или директориям.

    Возвращает:
        int: Количество директорий в списке.
    """
    directory_count = 0
    for path in path_list:
        if os.path.isdir(path):
            directory_count += 1
    return directory_count

# --- Примеры использования функции ---

# Создадим несколько фиктивных файлов и директорий для демонстрации
# В реальной ситуации вы будете работать с уже существующими путями.
test_dir1 = "test_dir_lab4"
test_file1 = "test_file_lab4.txt"

# Создаем директорию и файл (если их нет)
if not os.path.exists(test_dir1):
    os.makedirs(test_dir1)
with open(test_file1, 'w') as f:
    f.write("This is a test file.")

# Пример 1: Список с директориями, файлами и несуществующими путями
paths1 = [
    test_dir1,                  # Существующая директория
    test_file1,                 # Существующий файл
    "/non/existent/path",       # Несуществующий путь
    "."                         # Текущая директория
]
count1 = count_directories(paths1)
print(f"Список путей 1: {paths1}")
print(f"Количество директорий в списке 1: {count1}")
# Ожидаемый вывод: 2 (если '.' считается директорией)

# Пример 2: Пустой список
paths2 = []
count2 = count_directories(paths2)
print(f"\nСписок путей 2: {paths2}")
print(f"Количество директорий в списке 2: {count2}")
# Ожидаемый вывод: 0

# --- Очистка созданных фиктивных файлов и директорий (не часть функции) ---
if os.path.exists(test_file1):
    os.remove(test_file1)
if os.path.exists(test_dir1):
    os.rmdir(test_dir1)

