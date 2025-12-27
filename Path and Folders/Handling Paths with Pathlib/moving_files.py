from pathlib import Path
import shutil

filename = 'dad_jokes.txt'

src = Path.home() / "Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/copying_stuff" / filename
dest = Path.home() / "Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming"

if not(src.exists()):
    print("Source folder doesn't exist")
if not(dest.exists()):
    dest.mkdir(parents=True, exist_ok=True)
    shutil.move(src, dest)
else:
    shutil.move(src, dest)