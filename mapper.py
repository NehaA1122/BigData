import sys
import csv

# List of column numbers to remove
columns_remove = {6, 8, 11, 13, 14, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 38,
                  39, 40, 41, 43, 44, 46, 47, 48, 49, 54, 56, 57, 58, 59}  # Using a set for faster lookups

# Read input from stdin (Hadoop provides input data here)
reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')  # Change to `,` if CSV format

writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  # Output to stdout

# Filters header line based on columns to remove
header = next(reader)
filtered_header = [field for i, field in enumerate(header) if i not in columns_remove]

# Goes through each row in file
for fields in reader:
    try:
        # Removes specified columns
        filtered_fields = [field for i, field in enumerate(fields) if i not in columns_remove]

        # Extract relevant columns - airline and distance
        if len(filtered_fields) > 0:
            airline = filtered_fields[1]
            distance = filtered_fields[10]

            # Outputs airline and distance to stdout
            print(f"{airline}\t{distance}")

    # Skips lines with errors
    except Exception as e:
        continue
