import os
import random


folder_no = 0

ext = ['doc', 'ppt', 'pdf', 'hwp', 'jpg']

# quota 를 가지고서, 폴더에 들어간 후에, 남겨진 quota 를 다시 분배해서 들어가면 된다.


def make_random_folders(count):
    global folder_no

    if not count: return

    os.mkdir(f'folder{folder_no}')
    os.chdir(f'folder{folder_no}')

    folder_no += 1
    count -= 1
    while count:
        subcount = random.randint(0, count)
        make_random_folders(subcount)
        count -= subcount


report_home = 'w:/TestFolder'
#report_home = 'c:/TestFolder'

def make_random_root_folder():
    os.mkdir('root_folder')
    os.chdir('root_folder')
    make_random_folders(10)
    os.chdir('..')

#os.mkdir(report_home)
try:
    os.chdir(report_home)
except:
    try:
        os.mkdir(report_home)
    except:

make_random_root_folder()






