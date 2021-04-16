# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }

# Подумайте: полезен ли будет вам оператор распаковки?

def thesaurus(*args, key_sort = 'no'):
    dict_thesaurus = {}
    for word in args:
        if word[0] not in dict_thesaurus:
            dict_thesaurus[word[0]] = [word]
        else:
            dict_thesaurus[word[0]] += [word]
    print(dict_thesaurus)


thesaurus("Иван", "Мария", "Петр", "Илья")

# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(key_sort = 'no', *args):
    dict_thesaurus = {}
    if key_sort != 'yes':
        for word in args:
            if word[0] not in dict_thesaurus:
                dict_thesaurus[word[0]] = [word]
            else:
                dict_thesaurus[word[0]] += [word]
    else:
        for word in args:
            if word not in dict_thesaurus:
                dict_thesaurus[word] = [word[0]]
            else:
                dict_thesaurus[word] += [word[0]]
    print(dict_thesaurus)

thesaurus('yes', "Иван", "Мария", "Петр", "Илья")