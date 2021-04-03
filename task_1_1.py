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
print(days,"д",hours, "час", minutes, "мин", seconds, "сек")

