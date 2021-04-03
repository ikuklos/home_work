# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:

cube_of_odd_numbers_list = []
count = 0

while count <= 1000:
    if count % 2 != 0:
        cube_of_odd_numbers_list.append(count**3)
    count = count + 1

print(cube_of_odd_numbers_list)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!




sum_numbers=[]
for num in cube_of_odd_numbers_list:
    test_num = num
    work_list = []
    x = 1
    y = 0 < num // x <= 9
    count = 0
    while not y != False:
        x *= 10
        y = 0 < num // x <= 9

    while x >= 1:
        work_list.append(int(num//x))
        num -= x*work_list[count]
        x /= 10
        count += 1

    sum_all_list_numbers = 0
    for number_in_work_list in work_list:
        sum_all_list_numbers += number_in_work_list

    if sum_all_list_numbers%7 == 0:
        sum_numbers.append(test_num)
        sum_numbers.append(sum_all_list_numbers)

print(sum_numbers)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!!