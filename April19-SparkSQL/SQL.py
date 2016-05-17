# Spark example to print the average tweet length using Spark
# PGT April 2016   
# To run, do: spark-submit --master yarn-client SQL.py hdfs://hadoop2-0-0/data/twitter/part-03212

from __future__ import print_function
import sys, json
from pyspark import SparkContext
from pyspark.sql import SQLContext,Row

# Given a full tweet object, return the text of the tweet
def getInfo(line):
  try:
    js = json.loads(line)
    text = js['text'].encode('ascii', 'ignore')
    user = js['user']['screen_name']
    num_followers = js["user"]["followers_count"]
    return [(user,num_followers,text)]
  except Exception as a:
    return []
  
if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("enter a filename")
    sys.exit(1)
 
   
  sc = SparkContext(appName="tweetSearch")
  sqlContext = SQLContext(sc)
  
  tweets = sc.textFile(sys.argv[1])
  
  texts = tweets.flatMap(getInfo)
  
  df = sqlContext.createDataFrame(texts.map(lambda (u,f,t): Row(text = t, length = len(t), user = u, num_followers = f)))
  df.registerTempTable("tweets")
  
  print("DataFrame size %d" % df.count())
  
  matches = sqlContext.sql("SELECT * FROM tweets WHERE length < 55 AND num_followers > 10")
  print("Matches size %d" % matches.count())
  
  results = matches.take(10)
  for r in results:
    print(r)
  
  
  sc.stop()
