# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
# 100: (15, ['txt']),
# 1000: (3, ['py', 'txt']),
# 10000: (7, ['html', 'css']),
# 100000: (2, ['png', 'jpg']
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os

dir_struct = {}
all_sizes = {}
max_file_size = 0
start_point = 1
for root, dir, files in os.walk('my_project'):
    for file in files:
        all_sizes[file]=(os.stat(root+'/'+file).st_size)
        if os.stat(root+'/'+file).st_size > max_file_size:
            max_file_size = os.stat(root+'/'+file).st_size

print(all_sizes)

while start_point/10 <= max_file_size:
    dir_struct[start_point] = []
    start_point *= 10
#
# for size in all_sizes:
#     for key in sorted(dir_struct):
#         if size <= key:
#             dir_struct[key].append(size)
#             break
#             # all_sizes.remove(size)
# for key in all_sizes:
#     print(key)

for key in dir_struct:
    dir_struct[key] = (len(dir_struct[key]))

print(dir_struct)