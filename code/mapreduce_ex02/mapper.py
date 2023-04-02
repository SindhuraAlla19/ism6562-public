#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)

for line in sys.stdin:

    # remove leading and trailing whitespace

    line = line.strip()

    # split the line into integers
    values = [int(x) for x in line.split()]

    # emit each value with value and count
    for value in values:
        print('%d\t%d' % (value, 1))
