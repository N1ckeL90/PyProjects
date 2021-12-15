from random import choice, shuffle


def get_jokes(n, repeat=True):
    """
    Сreating a joke from 3 words

    :param n: number of jokes. If repeat=False then max 5 jokes
    :param repeat: allows the repetition of words in a joke
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    i = 0
    if repeat:
        while i < n:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1
        print(jokes)
    else:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for noun, adverb, adjective in zip(nouns, adverbs, adjectives):
            jokes.append(f'{noun} {adverb} {adjective}')
        print(jokes)


get_jokes(5)
get_jokes(5, repeat=False)
