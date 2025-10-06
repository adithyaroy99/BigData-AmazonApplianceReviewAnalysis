#!/usr/bin/python3
import sys

rating_counts = {}

for line in sys.stdin:
    try:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            rating = float(parts[0])
            count = int(parts[1])
            rating_counts[rating] = rating_counts.get(rating, 0) + count
    except:
        pass

for rating in sorted(rating_counts.keys(), reverse=True):
    print("{0}\t{1}".format(rating, rating_counts[rating]))