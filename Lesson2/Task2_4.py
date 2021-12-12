employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []
for el in employees:
    ind = el.rfind(" ")
    print(f'Привет, {el[ind + 1:].capitalize()}!')
