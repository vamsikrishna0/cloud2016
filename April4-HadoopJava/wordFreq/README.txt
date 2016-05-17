mkdir classes
hadoop com.sun.tools.javac.Main wordFrequency.java -d classes
hadoop jar wordFreq.jar wordFrequency /data/books b1
