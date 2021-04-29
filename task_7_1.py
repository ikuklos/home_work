# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#

import os

starter_directories = {'my_project_7_1' : ['settings', 'mainapp', 'adminapp', 'authapp']}
for key in starter_directories:
    if not os.path.exists(key):
        os.mkdir(key)
    os.chdir(key)
    for val in starter_directories[key]:
        if not os.path.exists(val):
            os.mkdir(val)


print(os.listdir())

