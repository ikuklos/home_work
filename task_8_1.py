# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.
#
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

dict_for_name_and_domen ={}

def email_parse(email_adress):
    re_email_data = re.compile('.+\@.+\..+')
    if len(re_email_data.findall(email_adress))>0:
        dict_for_name_and_domen['username'] = re.compile('.+\@').findall(email_adress)[0][0:-1]
        dict_for_name_and_domen['domain'] = re.compile('\@.+\..+').findall(email_adress)[0][1:]
    else:
        exit('Невалидный email - '+email_adress)
    print(dict_for_name_and_domen)


email_parse('123@yandex.ru')
email_parse('usrt@gb.ru')

email_parse('user@gmailru')

