#!/usr/bin/env python3
import csv
import sys

# Check if a filename is provided
if len(sys.argv) < 2:
    print("Usage: ./script_name.py input_file.csv")
    sys.exit(1)

input_filename = sys.argv[1]

filtered_rows = []

# Takes out any rows that have empty values-------------------


with open(input_filename, 'r') as file:
    reader = csv.reader(file)
    
    # Get the header (column names)
    header = next(reader)
    filtered_rows.append(header)

    for row in reader:
        # Check if there's any empty cell in the row
        if all(cell for cell in row):
            filtered_rows.append(row)

# Now, write the filtered_rows back to the same file
with open(input_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_rows)

#Creates a dictionary that counts how many times each county appears-----------------------------------------------

with open(input_filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    columns = {head: [] for head in header}
    for row in reader:
        for head, value in zip(header, row):
            columns[head].append(value)

counter = dict()
lessthan15 = list()

for county in columns['CountyName']:
    counter[county] = counter.get(county, 0) + 1

sCounties = [("County","Count")]
sCounties += (sorted(counter.items(), key=lambda x: x[1], reverse=True))

for item, value in sCounties[1:]:
    if value < 15:
        lessthan15.append(item)


#Filter out rows with counties that appear less than 15 times ---------------------------

filtered_rows = []

with open(input_filename, 'r') as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames
    filtered_rows.append(header)  # Append the header to the filtered rows list
    
    for row in reader:
        # Check if there's any empty cell in the row and if the county is not in the exclude list
        if all(row.values()) and row['CountyName'] not in lessthan15:
            filtered_rows.append(list(row.values()))

# Now, write the filtered_rows back to the same file or a new file
with open(input_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_rows)

# Creates csv file detailing each county and their respective count
with open("County_count.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sCounties)