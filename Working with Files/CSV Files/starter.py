import csv

def rating_category(rating):
    rating = int(rating)
    if rating <= -3:
        category = 'abysmal'
    elif rating <= -1:
        category = 'awful'
    else:
        category = 'bad'
    return category

modified_dad_jokes = []

with open('Documents/dad_jokes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    header.append('rating_category')
    modified_dad_jokes.append(header)
    for row in reader:
        row.append(rating_category(row[2]))
        modified_dad_jokes.append(row)

with open('Documents/modified_dad_jokes.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(modified_dad_jokes)