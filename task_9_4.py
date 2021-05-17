"""Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, turn_to):
        print(f'Машина повернула на {turn_to}')

    def show_speed(self):
        print('Текущая скорость:', self.speed)


test_car = Car(60, 'Red', 'SomeName')
test_car.go()
test_car.stop()
test_car.turn('лево')
test_car.show_speed()

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Разрешенная скорость 60 км/ч превышена! Текущая скорость -', self.speed)
        else:
            print('Текущая скорость:', self.speed)

town_test_car = TownCar(61, 'Yellow', 'Taxi')
town_test_car.show_speed()

class SportCar(Car):
    pass

sport_test_car = SportCar(60, 'RedBool', 'F1')
sport_test_car.turn('право')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Разрешенная скорость 40 км/ч превышена! Текущая скорость -', self.speed)
        else:
            print('Текущая скорость:', self.speed)


work_test_car = WorkCar(45, 'Ice', 'Ice Cube')
work_test_car.show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(self, speed, color, name)
        self.is_police = True

police_test_car = PoliceCar(145, 'White and Black', 'Cop')
print(police_test_car.is_police)