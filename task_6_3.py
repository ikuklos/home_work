# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#
# # Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# #
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи


names = list(open('task_6_3_names.csv', 'r', encoding='UTF-8'))


hobbys = list(open('task_6_3_hobbys.csv', 'r', encoding='UTF-8'))

names_and_hobbys = {}

count = 0
if len(hobbys) > len(names):
    print(1)
elif len(names) > len(hobbys):
    while len(names) > count:
        if len(hobbys) > count:
            names_and_hobbys[names[count]] = hobbys[count]
        else:
            names_and_hobbys[names[count]] = None
        count += 1
    print(count, names_and_hobbys)
else:
    while len(hobbys) > count:
        names_and_hobbys[names[count]] = hobbys[count]
        count += 1
    print(count, names_and_hobbys)


