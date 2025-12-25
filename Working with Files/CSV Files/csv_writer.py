# ['Max', 'Dog', 'bacon strips', 4754]
# ['Julius', 'Cat', 'catnip', 3215]
# ['Cal', 'Cat', 'anything edible', 71142]
# ['Lena', 'Cat', 'Sheba', 142]
# ['Bruiser', 'Featherfin Catfish', 'fish pellets', 54]

import csv

rows = [
    ['Max', 'Dog', 'bacon strips', 4754],
    ['Julius', 'Cat', 'catnip', 3215],
    ['Cal', 'Cat', 'anything edible', 71142],
    ['Lena', 'Cat', 'Sheba', 142],
    ['Bruiser', 'Featherfin Catfish', 'fish pellets', 54]
]

with open("Documents/expensive_pets.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name', 'species', 'favorite_snack', 'monthly_cost'])
    csv_writer.writerows(rows)

    # csv_writer.writerow(['Max', 'Dog', 'bacon strips', 4754])
    # csv_writer.writerow(['Julius', 'Cat', 'catnip', 3215])
    # csv_writer.writerow(['Cal', 'Cat', 'anything edible', 71142])
    # csv_writer.writerow(['Lena', 'Cat', 'Sheba', 142])
    # csv_writer.writerow(['Bruiser', 'Featherfin Catfish', 'fish pellets', 54])

