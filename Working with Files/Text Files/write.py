# Write method would OVERRIDE the file entirely.
with open("Documents/poem.txt", "w") as file:
    file.write("Roses are read,\n")
    file.write("Violets are blue,\n")
    file.write("Sugar is sweet,\n")
    file.write("And so are you!\n")