from pathlib import Path

###########################
# resolve() -> to show the absolute path.
# home() -> show the home directory (for each OS, the directory would be different).
# exists() -> Check if the directory/file exist or not.
# iterdir() -> Generates an iterator for files and folders within a directory.
###########################

current_dir = Path('.').resolve()
print(f"{current_dir} is the working directory")

home = Path.home()
print(f"{home} is the home directory")

doc_path = home / "Documents/Python Automations/Path and Folders/Handling Paths with Pathlib"
print(f"{doc_path} is the document directory")

file_path = doc_path / "my_file.txt"
print(f"{file_path} is the file path")

with open(file_path, 'r') as file:
    print(file.read())

# Parent Path of current director
print(current_dir.parent)