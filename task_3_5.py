# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов,
# взятых из трёх списков:
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]


def get_jokes(quantity):
    jokes = []
    while quantity >= 0:
        joke = random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives)
        jokes.append(joke)
        quantity -= 1
    print(jokes)

get_jokes(10)


# Документировать код функции.

# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
# _nouns = nouns.copy()
# print(_nouns)
# nun = _nouns[1]
# _nouns.remove(nun)
# print(_nouns)
# print(random.choice(_nouns))
# print(nouns[random.randrange(1,3 )])
def get_jokes(quantity, repeat='использовать'):
    _nouns = nouns.copy()
    _adverbs = adverbs.copy()
    _adjectives = adjectives.copy()
    jokes = []
    if repeat != 'неиспользовать':
        while quantity >= 0:
            noun = random.choice(_nouns)
            adverb = random.choice(_adverbs)
            adjective = random.choice(_adjectives)
            joke = f'{noun} {adverb} {adjective}'
            jokes.append(joke)
            quantity -= 1
    else:
        quantity = len(_nouns)
        while quantity > 0:
            noun = _nouns[random.randrange(0, quantity)]
            adverb = _adverbs[random.randrange(0, quantity)]
            adjective = _adjectives[random.randrange(0, quantity)]
            _nouns.remove(noun)
            _adverbs.remove(adverb)
            _adjectives.remove(adjective)
            joke = f'{noun} {adverb} {adjective}'
            jokes.append(joke)
            quantity -= 1

    print(jokes)

get_jokes(10, 'неиспользовать')
