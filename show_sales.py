import csv
from sys import argv


def add_sale(*args):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if len(args[0]) == 1:
            tmp = csv.reader(f)
            for el in tmp:
                print(*el)
        elif len(args[0]) == 2:
            tmp = csv.reader(f)
            for i in range(0, int(args[0][1])-1):
                next(tmp)
            for line in tmp:
                print(*line)
        elif len(args[0]) == 3:
            tmp = csv.reader(f)
            for i in range(0, int(args[0][1])-1):
                next(tmp)
            for line in tmp:
                if tmp.line_num == int(args[0][2])+1:
                    return
                print(*line)


if __name__ == '__main__':
    add_sale(argv)
