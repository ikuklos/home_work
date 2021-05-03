# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),не используя ключевое слово yield.

def odd_nums(some_number):
    some_gen = (number for number in range(1, some_number+1, 2))
    return some_gen

odd_to_5 = odd_nums(5)


print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
