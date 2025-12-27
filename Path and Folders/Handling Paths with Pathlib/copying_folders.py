from pathlib import Path
import shutil

src = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/another_new_folder'
dest = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/copying_stuff'

if not(src.exists()):
    print("Source folder doesn't exist")
else:
    shutil.copytree(src, dest, dirs_exist_ok=True)