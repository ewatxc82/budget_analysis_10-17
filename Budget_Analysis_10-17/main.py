import os
import csv

f = open('budget_data.csv')

csv_f = csv.reader(f)
next(csv_f, None)

months = []

for row in csv_f:
    months.append(row[0])

print(len(months))

f.close



