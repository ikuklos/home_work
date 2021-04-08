# Дан список:

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

temp_index_list = []

for item in some_list:
    for symbol in item:
        if symbol.isnumeric():
            temp_index_list.append(some_list.index(item))

for index_number in temp_index_list:
    if temp_index_list.count(index_number) > 1:
        temp_index_list.remove(index_number)

for index_number in temp_index_list:
    if int(some_list[index_number]) // 1 < 10:
        if len(some_list[index_number]) > 1:
            some_list[index_number] = '0'.join(some_list[index_number])
        else:
            some_list[index_number] = '0' + some_list[index_number]

for index_number in temp_index_list:
    index_number += 2 * temp_index_list.index(index_number)
    some_list.insert(index_number+1, '"')
    some_list.insert(index_number, '"')

print(some_list)

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

some_string = ' '.join(some_list)
print(some_string)

# Считается ли список с индексами как создание списка?
