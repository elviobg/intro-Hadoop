#!/usr/bin/python

# Format of each line is Common Log Format:
#
# We want elements 1 and 5
# We need to write them out to standard output, separated by a tab

import sys
import re

p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')
file = open('/home/training/udacity_training/data/1000_logs.txt', 'r')

for line in sys.stdin:
    m = p.match(line.strip())
    if not m:
        continue
    host, id, user, date, request, status, size = m.groups()
    data = request.strip().split(" ")
    if len(data) == 3:
      method, path, http = data   
      print "{0}\t{1}".format(host, 1)
