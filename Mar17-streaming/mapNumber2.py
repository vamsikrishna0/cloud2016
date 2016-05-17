#!/usr/bin/env python

import sys
import string

num_sum = 0
num_count = 0

for line in sys.stdin:
  number = line.strip()
  try:
    num_sum = num_sum + int(number)
    num_count = num_count + 1
  except:
    continue
  
print 'sum\t%s' % num_sum
print 'count\t%s' % num_count
