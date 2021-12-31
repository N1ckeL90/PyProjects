import os


root = os.path.dirname(__file__)
data_path = os.path.join(root, 'my_project')
result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]
for root, dirs, files in os.walk(data_path):
    for _file in files:
        sz = os.stat(os.path.join(root, _file)).st_size
        if sz == 0:
            result[0] += 1
        for i, key in enumerate(keys):
            if key < sz <= keys[i + 1]:
                result[keys[i + 1]] += 1
print(result)
