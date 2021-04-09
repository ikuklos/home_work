# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
sm_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки.
# Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!'

print('Вывести на экран фразы вида:')
for sort_item in sm_list:
    print('Привет,', sort_item.split()[-1] + '!')

# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.

print('\nПривести имена к корректному виду:')
for sort_item in sm_list:
    print('Привет,', sort_item.split()[-1].title() + '!')

# Можно ли при этом не создавать новый список?

print('\n"Можно ли при этом не создавать новый список?"'
      '\nФормально "sort_item.split()" является списком, если считаем так, то я бы сказал,'
      '\nчто можно, но через геморой со строками, что не рационально.'
      '\nЖду не дождусь разбора домашки.')