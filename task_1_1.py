# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:

duration = int(input("Введите время в секундах: "))

# до минуты: <s> сек;

print(duration, "сек")

# * до часа: <m> мин <s> сек;

minutes = duration // 60
seconds = duration % 60
print(minutes, "мин", seconds, "сек")

# * до суток: <h> час <m> мин <s> сек;

hours = minutes // 60
minutes = minutes - hours * 60
print(hours, "час", minutes, "мин", seconds, "сек")

# * *до месяца, до года, больше года: по аналогии.

days = hours // 24
hours = hours - days * 24
print(days, "д", hours, "час", minutes, "мин", seconds, "сек")

weeks = days // 7
days = days - weeks * 7
print(weeks, "нед", days, "д", hours, "час", minutes, "мин", seconds, "сек")

months = int(weeks // 4.33)
weeks = int(weeks - months * 4.33)
print(months, "мес", weeks, "нед", days, "д", hours, "час", minutes, "мин", seconds, "сек")

years = months // 12
months = months - years * 12
print(years, "г", months, "мес", weeks, "нед", days, "д", hours, "час", minutes, "мин", seconds, "сек")

# Пример вывода:
#
# Введите время в секундах: 456789123
# 456789123 сек
# 7613152 мин 3 сек
# 126885 час 52 мин 3 сек
# 5286 д 21 час 52 мин 3 сек
# 755 нед 1 д 21 час 52 мин 3 сек
# 174 мес 1 нед 1 д 21 час 52 мин 3 сек
# 14 г 6 мес 1 нед 1 д 21 час 52 мин 3 сек
