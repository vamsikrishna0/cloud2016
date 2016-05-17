#!/usr/bin/env python
import mincemeat

# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

file = open('mobydick.txt','r')
data = list(file)
file.close()


# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    for word in v.split():
      word = word.strip()
      if len(word) >= 1:
        yield word, 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []

for k in results.keys():
  resultlist.append((k,results[k]))
  
resultlist = sorted(resultlist, key=lambda a: a[1])

print resultlist[-5:]
