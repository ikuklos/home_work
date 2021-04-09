# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]

some_float_nums = [1.94, 12.83, 89, 76.9, 79.06, 01.36, 34.95, 2.25, 974.09, 61.1, 78.544, 1.12, 6.98, 45.00, 0, 0.00]

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).

one_string = ''

for price in some_float_nums:
    roubles = int(price // 1)
    price -= roubles
    kopecks = int(price * 100 // 1)
    one_string += str(roubles) + ' руб ' + str(kopecks) + ' коп, '

print(one_string)

# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).

one_string = '\n'

for price in some_float_nums:
    roubles = int(price // 1)
    price -= roubles
    if roubles < 10:
        roubles = "0" + str(roubles)
    kopecks = int(price * 100 // 1)
    if kopecks < 10:
        kopecks = "0" + str(kopecks)
    one_string += str(roubles) + ' руб ' + str(kopecks) + ' коп, '

print(one_string)

# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

print('\nАдрес объекта до сортировки -', id(some_float_nums))
some_float_nums.sort()
print('Отсортированные цены -', some_float_nums)
print('Адрес объекта после сортировки -', id(some_float_nums))

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

sort_up_to_down = list(reversed(some_float_nums))
print('\nОтсортированные от большего к меньшему', sort_up_to_down, '\nАдрес объекта', id(sort_up_to_down), '\n')

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print(sort_up_to_down[:4])
