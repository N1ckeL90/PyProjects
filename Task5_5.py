src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp = {}
for el in src:
    if el in tmp:
        tmp[el] = 1
    else:
        tmp[el] = 0
result = [el for el in src if tmp[el] == 0]
print(result)
