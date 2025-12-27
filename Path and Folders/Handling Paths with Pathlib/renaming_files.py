from pathlib import Path
import shutil

# current_file_name = 'dad_jokes.txt'
# new_file_name = 'bad_jokes.txt'

# src = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming' / current_file_name
# dest = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming' / new_file_name

current_file_name = 'bad_jokes.txt'
new_file_name = 'sad_jokes.txt'

src = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming' / current_file_name
dest = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming/123rd folder' / new_file_name

if not(src.exists()):
    print("Source folder doesn't exist")
else:
    shutil.move(src, dest)