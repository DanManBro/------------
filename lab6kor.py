import sqlite3
import os

def find_link_tables_sqlite(db_file):
    """
    Находит таблицы связки в базе данных SQLite.
    Таблица считается связкой, если её имя соответствует шаблону "таблица1_таблица2",
    и "таблица1" и "таблица2" существуют как отдельные таблицы.

    Args:
        db_file (str): Путь к файлу базы данных SQLite.

    Returns:
        list: Список наименований найденных таблиц связки.
              Возвращает пустой список при ошибках или отсутствии таких таблиц.
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Получаем все имена таблиц
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        all_table_names = [row[0] for row in cursor.fetchall()]
        
        # Для быстрого поиска
        all_table_names_set = set(all_table_names)

        link_tables = []
        for table_name in all_table_names:
            # Проверяем на одно нижнее подчеркивание
            if table_name.count('_') == 1:
                part1, part2 = table_name.split('_')
                # Проверяем существование обеих частей как отдельных таблиц
                if part1 in all_table_names_set and part2 in all_table_names_set:
                    link_tables.append(table_name)
        
        return link_tables

    except sqlite3.Error as e:
        print(f"Ошибка БД: {e}")
        return []
    finally:
        if connection:
            connection.close()


# --- Пример использования ---
if __name__ == "__main__":
    db_file_name = 'simple_test.db'

    # Удаляем старый файл БД, если он существует
    if os.path.exists(db_file_name):
        os.remove(db_file_name)

    # Создаем минимальный набор тестовых таблиц
    conn = sqlite3.connect(db_file_name)
    cursor = conn.cursor()
    
    print(f"Создаем тестовую БД '{db_file_name}' с таблицами...")
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("CREATE TABLE roles (id INTEGER PRIMARY KEY, role_name TEXT);")
    cursor.execute("CREATE TABLE users_roles (user_id INTEGER, role_id INTEGER, PRIMARY KEY (user_id, role_id));")
    cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, product_name TEXT);")
    # Добавим таблицу без связей для проверки
    cursor.execute("CREATE TABLE settings (id INTEGER PRIMARY KEY, value TEXT);")
    cursor.execute("CREATE TABLE products_settings (id INTEGER PRIMARY KEY, detail TEXT);") 
    # Добавим таблицу, которая содержит '_' но не является таблицей связки по нашим правилам
    cursor.execute("CREATE TABLE order_details (id INTEGER PRIMARY KEY, detail TEXT);")
    conn.commit()
    conn.close()
    print("Тестовые таблицы созданы.")

    # Вызываем функцию для поиска таблиц связки
    print("\nИщем таблицы связки...")
    found_links = find_link_tables_sqlite(db_file_name)

    if found_links:
        print(f"Найденные таблицы связки: {found_links}")
        # Ожидаемый вывод: ['users_roles']
    else:
        print("Таблицы связки не найдены.")

    # Очистка: удаляем созданный файл базы данных
    if os.path.exists(db_file_name):
        os.remove(db_file_name)
        print(f"\nТестовый файл БД '{db_file_name}' удален.")
