import csv
from sys import exit
from itertools import zip_longest


with open('users.csv', encoding='utf-8') as users_file:
    with open('hobby.csv', encoding='utf-8') as hobby_file:
        users = [",".join(el) for el in csv.reader(users_file)]
        hobby = [", ".join(el) for el in csv.reader(hobby_file)]
if len(hobby) > len(users):
    exit(1)
tmp = zip_longest(users, hobby, fillvalue=None)
result = dict(tmp)

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    for key, value in result.items():
        f.writelines(f'{key}: {value}\n')
