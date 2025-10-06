#!/usr/bin/python3
import sys
import json

for line in sys.stdin:
    try:
        review = json.loads(line.strip())
        rating = review.get('rating')
        if rating is not None:
            print("{0}\t1".format(rating))
    except:
        pass