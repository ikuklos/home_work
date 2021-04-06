# 3. Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем
# число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

number = int(input('Введите Ваше число: '))
root_word = 'процент'
ending = ['', 'ов', 'а']

#код для процентов больше 100
#if number >= 100:
#     num = number - number // 100 * 100
#     if num % 10 == 0 or num // 10 == 1:
#         print(number, 'процент' + ending[1])
#     elif 5 <= num - num // 10 * 10 <= 9:
#         print(number, 'процент' + ending[1])
#     elif 2 <= num - num // 10 * 10 <= 4:
#         print(number, 'процент' + ending[2])
#     elif num - num // 10 * 10 == 1:
#         print(number, 'процент' + ending[0])
# else:

if number % 10 == 0 or number // 10 == 1:
    print(number, 'процент' + ending[1])
elif 5 <= number - number // 10 * 10 <= 9:
    print(number, 'процент' + ending[1])
elif 2 <= number - number // 10 * 10 <= 4:
    print(number, 'процент' + ending[2])
elif number - number // 10 * 10 == 1:
    print(number, 'процент' + ending[0])
else:
    print('Введите число в диапазоне от 0 до 20')