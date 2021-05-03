# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
#
# Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# import requests
# open('task_6_1_all_logs.txt', 'w', encoding='UTF-8').writelines(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)

log_file = open('task_6_1_all_logs.txt', 'r', encoding='UTF-8')

list_ip_type_res = [(line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]) for line in log_file]
print(list_ip_type_res)

# для второго задания запишем результат в файл
import json
with open('task_6_1_ip_type_res.json', 'w', encoding='UTF-8') as f:
    json.dump(list_ip_type_res, f)
