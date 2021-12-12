count = 1
percent_names = ['процент', 'процента', 'процентов']
for i in range(1, 101):
    if 5 <= i <= 20 or i % 10 >= 5 or i == 100:
        print(i, percent_names[2])
    elif i == 1 or i % 10 == 1:
        print(i, percent_names[0])
    elif 2 <= i <= 4 or 2 <= i % 10 <= 4:
        print(i, percent_names[1])
