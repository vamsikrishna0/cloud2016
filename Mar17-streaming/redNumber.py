#!/usr/bin/env python

import sys
import string

word_count = 0
old_word = None

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if old_word != key:
    if old_word:
      print '%s\t%s' % ( old_word,word_count)
      word_count = 0
  old_word = key
  try:
    word_count = word_count + int(val)
  except:
    continue
print '%s\t%s' % (old_word,word_count)
