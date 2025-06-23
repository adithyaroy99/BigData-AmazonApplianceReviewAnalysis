#!/usr/bin/env python3
# Mapper Script - Computes % change in FX for each country over time

import sys

# Initialize variables
previousCountry = None
previousFx = None
fxMap = []

# Read from standard input
infile = sys.stdin
next(infile)  # Skip header line

for line in infile:
    try:
        line = line.strip()
        parts = line.split(',', 2)

        if len(parts) < 3:
            continue

        currentCountry = parts[1].strip()
        fxValue = parts[2].strip()
        if not fxValue:
            continue

        currentFx = float(fxValue)

        if currentCountry != previousCountry:
            previousCountry = currentCountry
            previousFx = currentFx
            continue

        # Compute percent change
        percentChange = ((currentFx - previousFx) / previousFx) * 100.0
        percentChange = round(percentChange, 2)

        currentKey = "{}: {:6.2f}%".format(currentCountry, percentChange)
        fxMap.append((currentKey, 1))

        previousCountry = currentCountry
        previousFx = currentFx

    except Exception as e:
        print("Error processing line: {}".format(line), file=sys.stderr)
        print("Exception: {}".format(e), file=sys.stderr)
        continue

# Emit output
for item in sorted(fxMap):
    print("{:<20s} - {}".format(item[0], item[1]))
