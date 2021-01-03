import csv
import os

emails = os.listdir('emails')

header = ["text", "spam"]

with open('MultitxtTocsv.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)  # write header
    for row in emails:
        f = open("emails/" + str(row))
        csv_writer.writerow([f.read()])  # write each row
