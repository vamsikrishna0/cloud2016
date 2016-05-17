# spark-submit --master yarn-client followersToLength.py hdfs://hadoop2-0-0/data/twitter/part-03212

# Spark program to see if there is a relationship between the number of followers a user has
# and the average length of their tweets.
#
# Will display a plot when done.  
# To display, you'll need to install matplotlib
# Execute this to install:  yum install python-matplotlib

from __future__ import print_function
import sys
import json
import matplotlib.pyplot as plt
from pyspark import SparkContext


# Function to extract the length of tweet text, screen name, 
# and number of followers from the stored json structure.
# One line per tweet.
def getText(line):
    try:
        js = json.loads(line)
        text = js["text"].encode('ascii', 'ignore')
        user = js["user"]["screen_name"]
        num_followers = js["user"]["followers_count"]
        if len(text) > 150:
          return []
        return [(user, len(text), int(num_followers))]
    except Exception as a:
        return []
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="FollowersToLength")
    
    tweets = sc.textFile(sys.argv[1], 40)
    
    # To speed testing, only deal with 1% of the tweets.
    #tweets = tweets.sample(True,0.01) 
    
    # For each line/tweet, extract the username, tweet text, and follower count.
    t = tweets.flatMap(getText)
    
    # Because t will get used again in multiple locations, cache this RDD in RAM througout
    # the cluster.  About a 4x speed up.
    t.cache()

    # Get the number of followers per user.  (user, # followers)  
    num_followers = t.map(lambda (user, t_len, followers): (user,followers)).reduceByKey(lambda a, b: a )
    
    # Get the number of tweets per user.  (user, # tweets)
    tweet_count = t.map(lambda (user,t_len, followers ): (user,1)).reduceByKey(lambda a, b: a + b)
    
    # Get the length of all the tweets per user.  Note we did not extract all text, but text length above.
    # (user, total tweet length)
    tweet_length = t.map(lambda (user, t_len, followers): (user,t_len)).reduceByKey(lambda a, b: a + b)
    
    # Find the average tweet length per user.  (user, avg tweet length)
    avg_len = tweet_length.join(tweet_count).map(lambda (user, (c, l)): (user, float(c)/l))
    
    # Now join the average tweet length RDD with the num followers RDD
    # (user, (avg len, # followers)
    avg_len_num_f = avg_len.join(num_followers, 10)
    
    print("Looking at %d tweets out of %d" % (t.count(), tweets.count()))
    
    # Retrieve the top 1000 users, based on the number of followers each has.
    data = avg_len_num_f.takeOrdered(1000, key=lambda a: -a[1][1])
    #print("%s" % str(data))
    
    # Extract the length of the tweets
    tlen = map(lambda a: a[1][0], data)
    # Extract the number of followers
    nfollow = map(lambda a: a[1][1], data)
    
    # Now plot x (length) to y (followers) via matplotlib
    plt.plot(tlen, nfollow, 'ro')
    plt.xlabel('Avg Tweet Length')
    plt.ylabel('Number of Followers')
    plt.show()
  
    # Stop your spark job.
    sc.stop()
