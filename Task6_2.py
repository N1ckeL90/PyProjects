dic = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tmp = line.split()
        if tmp[0] in dic:
            dic[tmp[0]] += 1
        else:
            dic[tmp[0]] = 1
n = 0
key = ''
for ip, count in dic.items():
    if count > n:
        key = ip
        n = count
print(f'IP адрес спамера: {key}. Количество запросов:{n}')
