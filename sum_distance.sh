#!/bin/bash

# Check if input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 input.csv"
    exit 1
fi

input_file="$1"

# Process CSV to sum distance per airline and add a header
echo "Airline,TotalDistance"
awk -F',' 'NR>1 {sum[$2] += $11} END {for (airline in sum) print airline "," sum[airline]}' "$input_file" | sort -t',' -k2 -nr
