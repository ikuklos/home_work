# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os, shutil
start_exploring = 'my_project'
for root, dirs, files in os.walk(start_exploring):
    for dir in dirs:
        if 'templates' in os.path.join(root) and root != 'my_project':
            rel_path = os.path.relpath(os.path.join(root, dir))
            for i in os.listdir(rel_path):
                if not os.path.exists('my_project/templates/'+dir):
                    os.mkdir('my_project/templates/'+dir)
                if not os.path.exists('my_project/templates/'+dir+'/'+i):
                    shutil.copy2(rel_path+'/'+i, 'my_project/templates/'+dir+'/')