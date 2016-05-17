#!/usr/bin/env python
import mincemeat

# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    import time
    for w in v.split():
        time.sleep(1)
        print w
        yield 'Count', 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
