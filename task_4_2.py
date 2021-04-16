# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import requests

def currency_rates(char_code):
    data_of_currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if char_code in data_of_currency:
        place_on_api = data_of_currency[data_of_currency.find(char_code):data_of_currency.find(char_code)+150]
        print(f'Цена одного {char_code} =', place_on_api[place_on_api.find('</Name><Value>')+14:place_on_api.find('</Value></Valute>')], 'руб.')
    else:
        print("Такая валюта не найдена.")

currency_rates('USD')
