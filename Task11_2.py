class MyOwnErr(Exception):
    pass


in_data1 = int(input('Введите делимое: '))
in_data2 = int(input('Введите делитель: '))
try:
    if in_data2 == 0:
        raise MyOwnErr("Нельзя делить на ноль!!!")
except MyOwnErr as err:
    print(err)
else:
    res = in_data1 / in_data2
    print(res)
