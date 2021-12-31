import os


MAIN_DIR_NAME = 'my_project'
DIR_NAMES = ['settings', 'mainapp', 'adminapp', 'authapp']

try:
    os.mkdir(MAIN_DIR_NAME)
except FileExistsError:
    pass
for i in range(len(DIR_NAMES)):
    dir_path = os.path.join(MAIN_DIR_NAME, DIR_NAMES[i])
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass
