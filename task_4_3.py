# *(вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import requests, datetime

def currency_rates(char_code):
    data_of_currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if char_code in data_of_currency:
        dd_mm_yyyy = data_of_currency[data_of_currency.find('Date="')+6:data_of_currency.find('Date="')+16].split('.')
        server_date = datetime.date(day = int(dd_mm_yyyy[0]), month = int(dd_mm_yyyy[1]), year = int(dd_mm_yyyy[2]))
        place_on_api = data_of_currency[data_of_currency.find(char_code):data_of_currency.find(char_code)+150]
        print(f'Цена одного {char_code} =', place_on_api[place_on_api.find('</Name><Value>')+14:place_on_api.find('</Value></Valute>')], f'руб. по состоянию на {server_date}')
    else:
        print("Такая валюта не найдена.")

currency_rates('USD')
