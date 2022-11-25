import csv

with open("brand_add.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0],row[1])