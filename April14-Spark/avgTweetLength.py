# Spark example to print the average tweet length using Spark
# PGT April 2016   
# To run, do: spark-submit --master yarn-client avgTweetLength.py hdfs://hadoop2-0-0/data/twitter/part-03212

from __future__ import print_function
import sys, json
from pyspark import SparkContext

# Given a full tweet object, return the text of the tweet
def getText(line):
  try:
    js = json.loads(line)
    text = js['text'].encode('ascii', 'ignore')
    return [text]
  except Exception as a:
    return []
  
if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("enter a filename")
    sys.exit(1)
   
  sc = SparkContext(appName="avgTweetLength")
  
  tweets = sc.textFile(sys.argv[1],)
  
  texts = tweets.flatMap(getText)
  lengths = texts.map(lambda l: len(l))
  
  # Just show 10 tweet lengths to validate this works
  print(lengths.take(10))
  # Print out the stats
  print(lengths.stats())
  
  # Save to your local HDFS folder
  lengths.saveAsTextFile("lengths")
  
  
  sc.stop()
