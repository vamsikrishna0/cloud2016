#!/bin/bash
hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/numbers -output $1 -file *.py -mapper mapNumber.py -reducer redNumber.py -combiner redNumber.py
