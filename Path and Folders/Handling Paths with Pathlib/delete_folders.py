from pathlib import Path
import shutil

folder_location = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/copying_stuff'

### To delete a folder that doesn't have any folders/files inside
if not folder_location.exists():
    print("Folder does not exist")
else:
    Path.rmdir(folder_location)
    print("Folder removed")

folder_location_with_files = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/new_folder/another_new_folder'

### To delete folder that has folders/files inside
if not folder_location_with_files.exists():
    print("Folder with extra files/folders does not exist")
else:
    shutil.rmtree(folder_location_with_files)
    print("Folder with extra files/folders removed")