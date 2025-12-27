from pathlib import Path

crazy_path = Path.home() / "I" / "dont" / "exist.csv"
print(crazy_path)

if crazy_path.exists():
    with open(crazy_path) as file:
        print(file.read())
else:
    print("File doesn't exist")
