def create_dict_from_lists(keys_list, values_list):
    
    result_dict = {}
    min_length = min(len(keys_list), len(values_list))

    for i in range(min_length):
        key = keys_list[i]
        value = values_list[i]
        result_dict[key] = value

    return result_dict

# Примеры использования функции
# 1. Оба списка одинаковой длины
list1_1 = ['a', 'b', 'c']
list1_2 = [1, 2, 3]
dict1 = create_dict_from_lists(list1_1, list1_2)
print(f"Пример 1 (одинаковая длина): {dict1}")
# Ожидаемый вывод: {'a': 1, 'b': 2, 'c': 3}

# 2. Первый список длиннее второго
list2_1 = ['apple', 'banana', 'cherry', 'date']
list2_2 = [100, 200, 300]
dict2 = create_dict_from_lists(list2_1, list2_2)
print(f"Пример 2 (keys_list длиннее): {dict2}")
# Ожидаемый вывод: {'apple': 100, 'banana': 200, 'cherry': 300}

# 3. Один из списков пуст (values_list пуст)
list3_1 = ['x', 'y', 'z']
list3_2 = []
dict3 = create_dict_from_lists(list3_1, list3_2)
print(f"Пример 3 (values_list пуст): {dict3}")
# Ожидаемый вывод: {}

# 4. Оба списка пусты
list4_1 = []
list4_2 = []
dict4 = create_dict_from_lists(list4_1, list4_2)
print(f"Пример 4 (оба списка пусты): {dict4}")
# Ожидаемый вывод: {}
