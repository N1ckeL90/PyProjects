result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        result.append((ln[0], ln[5][1:], ln[6]))
print(result)
