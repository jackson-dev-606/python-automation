# Append method would append lines into the file.

additional_lines = ['Stars up above, \n', 'Whisper words of love \n']

with open("Documents/poem.txt", "a") as file:
    file.write("The sun is bright,\n")
    file.write("On this lovely night,\n")
    file.writelines(additional_lines)
