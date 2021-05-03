
# (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
import json
with open('task_6_1_ip_type_res.json', 'r', encoding='utf-8') as f:
    list_ip_type_res = json.load(f)

ip_adress = [i[0] for i in list_ip_type_res]

uniq_ip_adress = []

for ip in ip_adress:
    if ip not in uniq_ip_adress:
        uniq_ip_adress.append(ip)

quantity_request = [ip_adress.count(ip) for ip in uniq_ip_adress]

print(sorted(list(zip(quantity_request, uniq_ip_adress)), reverse=True)[0:30])

