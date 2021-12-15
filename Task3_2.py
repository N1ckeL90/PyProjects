def num_translate_adv(text):
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
    new_text = ''
    if text.istitle():
        new_text = text.lower()
        new_text = translate.get(new_text)
        print(new_text.capitalize())
    else:
        print(translate.get(text))


user_input = input('Введите число на английском языке от 0 до 10: ')
num_translate_adv(user_input)

