# библиотеки использовать нельзя, напишем свой велик

# паршу текст в словарь, с условием что название папки не содержит точек
# (для данного задания сработает, а так, конечно, способ кривой, .idea тому пример)

roots_files_and_dir = []
how_deep = {}
how_much_branch = 0
count = 0
count_2 = 0

with open('config_file.yaml') as file:
    for line in file:
        if line != '\n':
            count += 1
            if line[:3] == '|--':
                how_deep[line[3:].rstrip()] = count
    file.seek(0)
    for line in file:
        if line != '\n':
            count_2 += 1
        print(how_deep)

print(how_deep)
print(count)
#
# with open('config_file.yaml', encoding='utf-8') as dir_struct_plain_text:
#     dir_structure = {}
#     for line in dir_struct_plain_text:
#         print(line.rstrip())
