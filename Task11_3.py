class MyOwnErr(Exception):
    pass


res = []
while True:
    in_data = input('Введите число: ')
    if in_data == 'stop':
        print(res)
        break
    try:
        if not in_data.isdigit():
            raise MyOwnErr(f"Ошибка ввода данных, '{in_data}' не является числом")
    except MyOwnErr as err:
        print(err)
    else:
        res.append(int(in_data))
