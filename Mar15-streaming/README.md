EECS Cloud Setup
=========

## Configuration changes to make on your cscloud host BEFORE using Hadoop/Spark

Add an alias for your local machine:

1. Execute `hostname` in the terminal and make a note of what it prints (should be what you named the machine when you created it)
2. Execute `gedit /etc/hosts &`
3. Add the name of your machine (that you determined in Step 1) to the first line: `127.0.0.1   myhostname  localhost`
4. Save the file and quit

Specify your Hadoop Username:

1. Execute `gedit ~/.bashrc &`
2. Find the line that starts with `export HADOOP_USER_NAME` (should be line 18)
3. Delete `changeme`, and replace it with your UC user ID
4. Save the file and quit
5. In order for the changes to take effect, **you must open a new terminal window**

# Streaming Hints #
==========
To test via pipes:
`cat input/* | ./map.py | sort | ./reduce.py`

To run on cluster:
`hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/books -output myoutput -file *.py -mapper mapWC.py -reducer reduceWC.py`

Be sure myoutput does not exit in your HDFS home folder.

`hadoop fs -ls `

`hadoop fs -ls /users/bob`

`hadoop fs -rmr bob`

`hadoop fs -put herefile hdfsfile`

`hadoop fs -cat hdfsfile`

`hadoop fs -get hdfsfile`

http://hadoop2-0-0:8088/cluster
