#!/bin/bash
hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/books -output $1 -file *.py -mapper mapWC.py -reducer reduceWC.py -combiner reduceWC.py
