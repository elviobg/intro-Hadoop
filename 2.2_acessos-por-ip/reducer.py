#!/usr/bin/python

import sys

totalHits = 0
oldKey = None
pathSearching = '10.99.99.186'
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
	if pathSearching in oldKey:
   	  print oldKey, "\t", totalHits
        totalHits = 0

    oldKey = thisKey
    totalHits += 1

if pathSearching in oldKey:
    print oldKey, "\t", totalHits

