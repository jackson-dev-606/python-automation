from pathlib import Path
from datetime import datetime

# Path to iterate over
path = Path.home() / 'Python Automations/Path and Folders/Handling Paths with Pathlib/'
# print(path)

for item in path.iterdir():
    if item.is_file() and item.suffix == '.py':
        print(f"{item.name} is a file and the file type is {item.suffix}")
        print(f"{item.stem} is the name of the file.")
        stats = item.stat()
        print(f"Size: {stats.st_size} bytes")
        print(f"Last Modified: {datetime.fromtimestamp(item.stat().st_mtime)}")
    elif item.is_dir():
        print(f"{item.name} is a directory")

    if 'my_file' in item.name.lower():
        print(f"{item.name} contains the word 'my_file'")