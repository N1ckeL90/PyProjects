odd_cubes_list = []
total_sum = 0
# Создаем список кубов нечетных чисел от 1 до 1000
for i in range(1, 1001):
    if i % 2 != 0:
        i = i ** 3
        odd_cubes_list.append(i)
# Поиск элементов, сумма которых делится нацело на 7
for i in range(len(odd_cubes_list)):
    temp_var = 1
    sum_numbers = 0
    while temp_var < 1000000000:
        one_number = odd_cubes_list[i] // temp_var % 10
        sum_numbers += one_number
        temp_var = temp_var * 10
    if sum_numbers % 7 == 0:
        total_sum += odd_cubes_list[i]
print(total_sum)
# Прибавляем к исходному списку + 17
for i in range(len(odd_cubes_list)):
    odd_cubes_list[i] += 17
# Повторяем поиск суммы
total_sum = 0
for i in range(len(odd_cubes_list)):
    temp_var = 1
    sum_numbers = 0
    while temp_var < 1000000000:
        one_number = odd_cubes_list[i] // temp_var % 10
        sum_numbers += one_number
        temp_var = temp_var * 10
    if sum_numbers % 7 == 0:
        total_sum += odd_cubes_list[i]
print(total_sum)
