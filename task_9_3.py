"""Реализовать базовый класс Worker (работник):

определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};

создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров."""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}
        self._income['wage'] = wage
        self._income['bonus'] = bonus
        # print(self.name, self.surname, self.position, self._income)


sidorov = Worker('Иван', 'Сидоров', 'Разнорабочий', 50000, 50000)


class Position(Worker):
    def get_full_name(self):
        _full_name = f'{self.name} {self.surname}'
        print(_full_name)

    def get_total_income(self):
        _total_income = self._income['wage'] + self._income['bonus']
        print(_total_income)


petrov = Position('Олег', 'Иванов', 'Сантехник', 50000, 51000)


petrov.get_full_name()

petrov.get_total_income()
