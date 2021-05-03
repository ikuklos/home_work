# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

_temp_list = []
not_unique = []
for element in src:
    if element not in _temp_list:
        _temp_list.append(element)
    else:
        not_unique.append(element)

result = [unique_element for unique_element in src if unique_element not in not_unique]

print(result)

# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации

