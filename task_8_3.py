# Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:

# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
# Примечание: сможете ли вы замаскировать работу декоратора?
import functools

def val_checker(some_function_check):
    def inside_val_checker(function):
        functools.wraps(function)
        def type_logger(*args):
            if some_function_check(args[0]):
                return function(args[0])
            else:
                raise ValueError
        return type_logger
    return inside_val_checker

@val_checker(lambda num: num > 0)
def calc_cube(num):
    return num ** 3

a = calc_cube(4)
print(a)

b = calc_cube(-3)
