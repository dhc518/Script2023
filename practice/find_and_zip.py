import os
import datetime
import zipfile
import random


def make_random_folder(root_folder, depth=3, breadth=2):
    exts = ['doc', 'ppt', 'pdf', 'hwp', 'jpg']
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)
    for i in range(breadth):
        sub_folder = os.path.join(root_folder, f'sub_folder_{i}')
        if not os.path.exists(sub_folder):
            os.makedirs(sub_folder)
        if depth > 1:
            make_random_folder(sub_folder, depth-1, breadth)
        for j in range(breadth):
            for k in range(5):
                rand_num = random.randint(1, 1000)
                file_name = f'file{rand_num:03d}.{exts[k]}'
                with open(os.path.join(sub_folder, file_name), 'w') as f:
                    f.write(f'This is a {exts[k]} file.')

def zip_jpg(folder_path):
    zip_path = 'final.zip'
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.jpg'):
                    file_path = os.path.join(root, file)
                    file_name = os.path.splitext(os.path.basename(file_path))[0]
                    date = datetime.datetime.now().strftime('%Y%m%d')
                    new_name = f"{file_name}_{date}.jpg"
                    zip_file.write(file_path, arcname=new_name)
    print(f'압축 완료: {zip_path}')


make_random_folder('root_folder')
zip_jpg('root_folder')
