# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:

cube_of_odd_numbers_list = []
count = 0
for number_1 in range(1001):
    if number_1 % 2 != 0:
        cube_of_odd_numbers_list.append(number_1**3)

print(cube_of_odd_numbers_list)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!

sum_numbers_mod_7 = 0
for number_2 in cube_of_odd_numbers_list:

    cube_list_number = number_2
    bit_depth = 1
    depth_length_chek = 0 < number_2 // bit_depth <= 9
    while depth_length_chek != True:
        bit_depth *= 10
        depth_length_chek = 0 < number_2 // bit_depth <= 9

    work_list = []
    count = 0
    while bit_depth >= 1:
        work_list.append(number_2 // bit_depth)
        number_2 -= bit_depth * work_list[count]
        bit_depth //= 10
        count += 1

    sum_work_list_numbers = 0
    for number_in_work_list in work_list:
        sum_work_list_numbers += number_in_work_list

    if sum_work_list_numbers % 7 == 0:
        sum_numbers_mod_7 += cube_list_number

print(sum_numbers_mod_7) #17485588610

# К каждому элементу списка добавить 17

for number_3 in range(len(cube_of_odd_numbers_list)):
    cube_of_odd_numbers_list[number_3] += 17

print(cube_of_odd_numbers_list)

# и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!!

sum_numbers_mod_7 = 0
for number_2 in cube_of_odd_numbers_list:

    cube_list_number = number_2
    bit_depth = 1
    depth_length_chek = 0 < number_2 // bit_depth <= 9
    while depth_length_chek != True:
        bit_depth *= 10
        depth_length_chek = 0 < number_2 // bit_depth <= 9

    work_list = []
    count = 0
    while bit_depth >= 1:
        work_list.append(number_2 // bit_depth)
        number_2 -= bit_depth * work_list[count]
        bit_depth //= 10
        count += 1

    sum_work_list_numbers = 0
    for number_in_work_list in work_list:
        sum_work_list_numbers += number_in_work_list

    if sum_work_list_numbers % 7 == 0:
        sum_numbers_mod_7 += cube_list_number

print(sum_numbers_mod_7) #15392909930
