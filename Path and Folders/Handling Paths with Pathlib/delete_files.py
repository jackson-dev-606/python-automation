from pathlib import Path
import shutil

file_to_delete = 'testfile.txt'
file_location = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/moving_n_renaming/123rd folder' / file_to_delete

if not file_location.exists():
    print("File does not exist")
else:
    file_location.unlink()