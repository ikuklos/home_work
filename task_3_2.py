# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_name_transl(same_word):
    # same_word = str(same_word)
    # print(same_word)
    num_dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',  'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    ru_word = str(num_dictionary.get(same_word.lower()))
    if same_word[0].istitle():
        return ru_word[0].title() + ru_word[1:]
    else:
        return ru_word


print(num_name_transl('Zero'))
