from pathlib import Path
import shutil

filename = 'dad_jokes.txt'

src = Path.home() /'Python Automations/Path and Folders/Absolute Vs Relative Path/absolute_v_relative'/ filename
dest = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/copying_stuff'
dest_file_path = dest / filename

dest.mkdir(parents=True, exist_ok=True)

if not(src.exists()):
    print("Source file doesn't exist")
elif dest_file_path.exists():
    print("File exists in the destination folder")
else:
    shutil.copy(src, dest)
