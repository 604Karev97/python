import os
import shutil

ROOT = os.path.dirname(__file__)

dir_name = 'my_project'
temp_name = 'templates'
myproj_path = os.path.join(ROOT, dir_name)
temp_path = os.path.join(myproj_path, temp_name)

if not os.path.exists(temp_path):
    # os.mkdir(temp_path)
    print(temp_path)

try:
    for dr in os.scandir(myproj_path):
        if dr.is_dir():
            app_path = os.path.join(myproj_path, dr)
            for item in os.scandir(app_path):
                if item.is_dir():
                    dr_path = os.path.join(app_path, item)
                    for el in os.scandir(dr_path):
                        if el.is_dir():
                            el_path = os.path.join(dr_path, el)
                            shutil.copytree(dr_path, f'{dir_name}/templates/{el.name}')
except FileExistsError:
    print('Невозможно создать файл, так как он уже существует')
