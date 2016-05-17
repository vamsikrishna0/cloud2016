#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
  words = line.strip().lower().translate(None,string.punctuation).split()
  for word in words:
      print '%s\t%s' % (word, 1)
      print 'WordCount\t1'
