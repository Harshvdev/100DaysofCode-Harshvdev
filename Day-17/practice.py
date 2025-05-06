import os
import shutil
if not os.path.exists("Harsh-folder"):
    os.mkdir("Harsh-Folder")
    os.mkdir(f"Harsh-Folder/Day-{dir}")

delete_input = input("Do you want to delete the folders you just made? [y/n]").lower()

if delete_input == 'y':
    shutil.rmtree(f"Harsh-Folder")
