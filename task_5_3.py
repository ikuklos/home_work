import itertools
# Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'qwerg', 'sasda'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses
# меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

def pairs_maker(list_1, list_2):
    if len(tutors) > len(klasses):
        for (tutor, klass) in itertools.zip_longest(list_1, list_2):
            yield (tutor, klass)
    else:
        for (tutor, klass) in zip(list_1, list_2):
            yield (tutor, klass)

exhaustion_test = pairs_maker(tutors, klasses)

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))

print(next(exhaustion_test))


