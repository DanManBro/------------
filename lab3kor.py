def get_unique_elements_from_list(input_list):
    
    return list(item for item in set(input_list))


list1 = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list1 = get_unique_elements_from_list(list1)
print(f"Оригинальный список: {list1}")
print(f"Уникальные элементы: {unique_list1}")

list2 = ['apple', 'banana', 'apple', 'cherry', 'banana']
unique_list2 = get_unique_elements_from_list(list2)
print(f"\nОригинальный список: {list2}")
print(f"Уникальные элементы: {unique_list2}")

# 4. Пустой список
list4 = []
unique_list4 = get_unique_elements_from_list(list4)
print(f"\nОригинальный список: {list4}")
print(f"Уникальные элементы: {unique_list4}")
# Ожидаемый вывод: []

