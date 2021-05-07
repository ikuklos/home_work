# Написать декоратор для логирования типов позиционных аргументов функции, например:

# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3

# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
#
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?



def type_loger(function):
    def type_logger(*args):
        if len(args) > 0:
            for element in args:
                print(f'{element}: {type(element)},')
            return function(args[0])
    return type_logger

@type_loger
def calc_cube(num):
    return num ** 3

a = calc_cube(3, 6.0, 'text')


# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_loger(function):
    def type_logger(*args):
        if len(args) > 0:
            for element in args:
                print(f'{function.__name__}({element}: {type(element)})')
            return function(args[0])
    return type_logger

@type_loger
def calc_cube(num):
    return num ** 3

b = calc_cube(5)
