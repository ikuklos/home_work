import sys
from task_4_3 import currency_rates

if len(sys.argv) > 1:
    command_line_arg = sys.argv[1]
    currency_rates(command_line_arg)

# пример работы скрипта в терминале:
# (venv) D:\yadisk\YandexDisk\Documents\learn\IT\python\gb_learning\kuku_serj_dz>task_4_5.py USD
# 75,55 2021-04-17
