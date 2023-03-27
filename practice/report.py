import os
print(os.getcwd())
# for fn in os.listdir():
#     print(f'{os.path.dirname(fn)} {os.path.getsize(fn)}')

# for root, subfolders, filenames in os.walk('d:/python'):
#     print(f'ROOT:{root}'.center(80,'='))
#     print('Subfolders: '.ljust(15), subfolders)
#     print('Files: '.ljust(15), filenames)
#     print('\n')

files = [((name, os.path.getsize(os.path.join(root, name))) for name in filenames) for root, filenames in os.listdir('d:/python')]

files.sort(key=lambda s: s[1], reverse=True)
with open("report.txt", "w") as f:
    for name, size in files:
        f.write(f"{name} ({size} bytes)\n")


