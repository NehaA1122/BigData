import sys

airline_totals = {}

for line in sys.stdin:
    # Splits the input into 2
    parts = line.strip().split("\t")
    # If input is not 2 fields, skips
    if len(parts) != 2:
        continue

    # Categorises each part of input
    airline, distance = parts

    try:
        # Converts distance to float so can be summed
        distance = float(distance)
    except ValueError:
        # Skips invalid distances
        continue

    # If airline is in dictionary, increments distance
    if airline in airline_totals:
        airline_totals[airline] += distance
    # otherwise sets distance to distance already there
    else:
        airline_totals[airline] = distance

# Sorts and stores top 10 airlines
top_10 = sorted(airline_totals.items(), key=lambda x: x[1], reverse=True)[:10]

# Prints results
for airline, total_distance in top_10:
    print(f"{airline}\t{total_distance}")
