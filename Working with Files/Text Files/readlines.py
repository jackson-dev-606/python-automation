with open("Documents/dad_jokes.txt", 'r') as file:
    for line in file.readlines():
        print(line.strip())