import os
folders = input("please provide list of folders").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide valid folder name")
        continue    
        print("=== listing files for folder-" + folder)
    
    for file in files:
        print(file)

