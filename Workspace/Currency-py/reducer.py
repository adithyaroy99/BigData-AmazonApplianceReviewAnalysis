#!/usr/bin/env python3
# Reducer Script - Aggregates counts of % change occurrences

import sys

currentKey = None
currentCount = 0

for line in sys.stdin:
    try:
        line = line.strip()
        if not line:
            continue

        key, value = line.rsplit(' - ', 1)
        value = int(value)

        if key == currentKey:
            currentCount += value
        else:
            if currentKey is not None:
                print("{} - {}".format(currentKey, currentCount))
            currentKey = key
            currentCount = value

    except Exception as e:
        print("Error processing line: {}".format(line), file=sys.stderr)
        print("Exception: {}".format(e), file=sys.stderr)
        continue

# Print last key
if currentKey is not None:
    print("{} - {}".format(currentKey, currentCount))
