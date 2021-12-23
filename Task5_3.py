from itertools import zip_longest
#TUTORS = [
#    'Иван', 'Анастасия', 'Петр', 'Сергей',
#    'Дмитрий', 'Борис', 'Елена'
#]
TUTORS = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Николай', 'Екатерина'
]
KLASSES = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(TUTORS) < len(KLASSES):
    result = (text for text in zip(TUTORS, KLASSES))
    for i in range(1, len(TUTORS) + 2):
        try:
            print(next(result))
        except StopIteration:
            print("StopIteration")
else:
    result = (text for text in zip_longest(TUTORS, KLASSES, fillvalue=None))
    for i in range(1, len(KLASSES) + 2):
        try:
            print(next(result))
        except StopIteration:
            print("StopIteration")


