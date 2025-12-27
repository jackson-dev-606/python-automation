from pathlib import Path

current_dir = Path('.').resolve()
print(current_dir)

new_folder = current_dir / 'new_folder'

##############################################################################################
# mkdir -> to create a new folder.
# exist_ok = True -> If the folder exists, it won't create a new folder.
# parents = True -> If new folder has any parent folder's that don't exist, create those too.
##############################################################################################

new_folder.mkdir(exist_ok=True)

another_new_folder = new_folder / 'another_new_folder' / 'third_folder'
another_new_folder.mkdir(exist_ok=True, parents=True)