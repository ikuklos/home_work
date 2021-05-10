"""Создать класс TrafficLight (светофор):
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    _color = ('red', 'yellow', 'green')

    @staticmethod
    def running():
        for color in cycle('ryg'):
            if color == 'r':
                print('traffic light is now', TrafficLight._color[0])
                sleep(7)
            elif color == 'y':
                print('traffic light is now', TrafficLight._color[1])
                sleep(2)
            elif color == 'g':
                print('traffic light is now', TrafficLight._color[2])
                sleep(10)

    # def night_work(self):
    #     while True:
    #         print(TrafficLight._color[1])
    #         sleep(0.5)
    #         print('Black')
    #         sleep(0.5)


avenue_7 = TrafficLight()


avenue_7.running()
