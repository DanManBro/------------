import json

def json_string_to_dict(json_string):
    """
    Принимает JSON-строку и конвертирует её в Python-словарь.

    Args:
        json_string (str): Строка в формате JSON.

    Returns:
        dict or None: Сформированный словарь в случае успеха,
                      или None, если строка не является корректным JSON.
    """
    try:
        # json.loads() парсит JSON-строку и возвращает Python-объект (словарь, список и т.д.)
        data_dict = json.loads(json_string)
        return data_dict
    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании JSON-строки: {e}")
        return None
    except TypeError as e:
        print(f"Ошибка типа: Входные данные должны быть строкой. {e}")
        return None

# --- Примеры использования функции ---

# 1. Корректная JSON-строка, представляющая словарь
json_str1 = '{"name": "Alice", "age": 30, "city": "New York"}'
dict1 = json_string_to_dict(json_str1)
print(f"Пример 1 (корректный JSON-словарь): {dict1}")
print(f"Тип результата: {type(dict1)}\n")
# Ожидаемый вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 2. Некорректная JSON-строка (ошибка синтаксиса)
json_str3 = '{"name": "Bob", "age": 25, "city": "London",}' # Лишняя запятая в конце
dict3 = json_string_to_dict(json_str3)
print(f"Пример 3 (некорректный JSON): {dict3}\n")
# Ожидаемый вывод: Ошибка при декодировании JSON-строки: Expecting property name enclosed in double quotes: line 1 column 40 (char 39)

# 3. Пустая строка
json_str5 = ''
dict5 = json_string_to_dict(json_str5)
print(f"Пример 5 (пустая строка): {dict5}\n")
# Ожидаемый вывод: Ошибка при декодировании JSON-строки: Expecting value: line 1 column 1 (char 0)

