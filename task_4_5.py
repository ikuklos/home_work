import sys
from task_4_3 import currency_rates

if len(sys.argv) > 1:
    command_line_arg = sys.argv[1]
    currency_rates(command_line_arg)