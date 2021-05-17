"""Реализовать класс Stationery (канцелярская принадлежность):
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки')


test_stat = Stationery()
print(test_stat.title)
test_stat.draw()


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


test_pen = Pen()
print(test_pen.title)
test_pen.draw()


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


test_pencil = Pencil()
print(test_pencil.title)
test_pencil.draw()


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


test_handle = Handle()
print(test_handle.title)
test_handle.draw()