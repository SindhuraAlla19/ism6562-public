#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    numbers = line.split()
    # increase counters
    total = 0
    count = 0
    for num in numbers:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        total += int(num)
        count += 1
    print '%s\t%s' % ("line_total", total)
    print '%s\t%s' % ("line_count", count)

