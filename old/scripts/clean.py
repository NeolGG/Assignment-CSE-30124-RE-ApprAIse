#!/usr/bin/env python3
import csv
import sys
import datetime as dt

#cleans king_county data

# Check if a filename is provided
if len(sys.argv) < 2:
    print("Usage: ./script_name.py input_file.csv")
    sys.exit(1)

input_filename = sys.argv[1]

filtered_rows = []

# Takes out any rows that have empty values-------------------

with open(input_filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    filtered_rows.append(header)

    for row in reader:
        if all(cell and cell != "?" for cell in row): # Check if there's any empty cell in the row
            filtered_rows.append(row)

        # if int(float(row[12])):
        #     row[11] = str(int(float(row[11])) - 5475)
        
        # if int(float(row[13])):
        #     date1 = dt.date(int(float(row[13])),1,1)
        #     date2 = dt.date(2016,1,1) #fake date for the model 

        #     diff = date2 - date1
        #     print(diff.days)
        #     row[13] = str(diff.days)

        # date1 = dt.date(int(row[12]),1,1)
        # date2 = dt.date(2016,1,1) #fake date for the model 

        # diff = date2 - date1
        # print(diff.days)
        # row[12] = str(diff.days)

with open(input_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_rows)


