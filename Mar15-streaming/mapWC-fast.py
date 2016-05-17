#!/usr/bin/env python

import sys
import string

wordd = {}
count = 0

for line in sys.stdin:
  words = line.strip().lower().translate(None,string.punctuation).split()
  for word in words:
      if word in wordd.keys():  # may be slow
        wordd[word] = wordd[word] + 1
      else:
        wordd[word] = 1
      count = count + 1

for k in wordd.keys():
  print '%s\t%s' % (k, wordd[k])
print 'WordCount\t%s' % count
