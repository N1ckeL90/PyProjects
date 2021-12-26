from sys import argv
import csv


def add_sale(price):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        file_writer = csv.writer(f, lineterminator='\r')
        file_writer.writerow([price])


if __name__ == '__main__':
    add_sale(argv[1])
