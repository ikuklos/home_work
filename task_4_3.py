# *(вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import requests, datetime

print(datetime.datetime(17, month04, year=2021))
def currency_rates(char_code):
    data_of_currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if char_code in data_of_currency:

        place_on_api = data_of_currency[data_of_currency.find(char_code):data_of_currency.find(char_code)+150]
        print(f'Цена одного {char_code} =', place_on_api[place_on_api.find('</Name><Value>')+14:place_on_api.find('</Value></Valute>')], 'руб.')
    else:
        print("Такая валюта не найдена.")

currency_rates('USD')
