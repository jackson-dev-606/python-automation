from pathlib import Path
import shutil

current_folder_name = 'third_folder'
new_folder_name = '123rd folder'

src = Path.home() / 'Library/Mobile Documents/com~apple~CloudDocs/Zero To Mastery/Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming' / current_folder_name
dest = Path.home() / 'Library/Mobile Documents/com~apple~CloudDocs/Zero To Mastery/Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming' / new_folder_name

if not(src.exists()):
    print("Source folder doesn't exist")
else:
    shutil.move(src, dest)