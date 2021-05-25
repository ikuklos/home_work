# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым эл. первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, user_input):
        self.matrix = user_input

    def __str__(self):
        return '\n'.join([' '.join(map(str, part)) for part in self.matrix])

    def __add__(self, other):
        new_matrix_2 = []
        for string_1, string_2 in zip(self.matrix, other.matrix):
            temp_string = [val_1 + val_2 for val_1, val_2 in zip(string_1, string_2)]
            new_matrix_2.append(temp_string)
        return '\n'.join([' '.join(map(str, part)) for part in new_matrix_2])


test_matrix_1 = Matrix([[32, 22, 2], [37, 43, 13], [51, 86, 12]])
test_matrix_2 = Matrix([[1, 2], [3, 4], [5, 6]])

print(test_matrix_1, '\n')
print(test_matrix_2+test_matrix_1)
