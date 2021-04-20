# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
# Подсказка: использовать возможности python, изученные на уроке.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

result = (priveus_number for num in src if src.index(num) > 0) < (priveus_number for num in src if src.index(num) > 0)

print(result)

result = [
    number for number in src if src.index(number) > 0 and src.index(number) <= len(src) and number > src[next(index - 1 for index in range(len(src)))]
]

print(result)

