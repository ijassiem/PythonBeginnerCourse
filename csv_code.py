import csv

with open('data1.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
