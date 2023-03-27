#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

total = 0
count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        value = int(value)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if key == 'line_total':
        total += value
    elif key == 'line_count':
        count += value
    else:
        continue
print '%s\t%s' % ("average",total/count)
