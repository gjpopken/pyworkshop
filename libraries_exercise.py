import os

my_folder = os.getcwd()
print(f'This is the current working directory: {my_folder}')

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f' - {entry.name}')

# This also works:
# folder_contents = os.scandir(my_folder)
# for entry in folder_contents:
#     print(f' - {entry.name}')