def num_translate(text):
    translate = {'zero': 'ноль',
                 'one': 'один',
                 'two': 'два',
                 'three': 'три',
                 'four': 'четыре',
                 'five': 'пять',
                 'six': 'шесть',
                 'seven': 'семь',
                 'eight': 'восемь',
                 'nine': 'девять',
                 'ten': 'десять'}
    print(translate.get(text))


user_input = input('Введите число на английском языке от 0 до 10: ')
num_translate(user_input)
