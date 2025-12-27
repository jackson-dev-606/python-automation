from pathlib import Path
import shutil

src = Path.home() / "Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/copying_stuff/third_folder"
dest = Path.home() / "Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming/"

if not(src.exists()):
    print("Source folder doesn't exist")
elif not(dest.exists()):
    print("Destination folder doesn't exist")
else:
    shutil.move(src,dest)