from random import choice
from pprint import pprint


def get_jokes(n, flag=True):
    """
    Get jokes from three lists of nouns, adverbs and adjectives
    :param n: count of jokes
    :param flag: True - repeat same words
                 False - don't repeat same words
    :return: list of jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    try:
        for i in range(n):
            if flag == True:
                joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
                jokes.append(joke)
            else:
                noun = choice(nouns)
                adverb = choice(adverbs)
                adjective = choice(adjectives)
                joke = f'{noun} {adverb} {adjective}'
                jokes.append(joke)
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
    except IndexError:
        print('Слишком большое чилсо "n"')
    return jokes


pprint(get_jokes(10, flag=False))
print(help(get_jokes))
