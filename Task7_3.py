import os
import shutil


root_dir = os.path.join(os.path.dirname(__file__), 'my_project')
dst_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')
try:
    os.makedirs(dst_dir)
except FileExistsError:
    pass
for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir_ in dirs:
            try:
                os.makedirs(os.path.join(dst_dir, dir_))
            except FileExistsError:
                pass
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_dir, os.path.basename(root))
            if not os.path.dirname(src_file) == dst_file:
                shutil.copy(src_file, dst_file)
