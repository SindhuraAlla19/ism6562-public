#!/usr/bin/env python

"""reducer.py"""

import sys

# input comes from STDIN (standard input)

total_sum = 0

total_count = 0

for line in sys.stdin:

    # remove leading and trailing whitespace

    line = line.strip()

    # parse the input we got from mapper.py

    value, count = line.split('\t', 1)

    try:

        # convert count (currently a string) to int
        value = int(value)
        count = int(count)

        # accumulate the sum of values and the count of values

        total_sum += value * count

        total_count += count

    except ValueError:

        # count was not a number, so silently ignore this line

        pass

# calculate the average value

average = float(total_sum) / total_count

# output the final result to STDOUT

print('Average value: %f' % average)
