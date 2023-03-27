#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -files mapper.py, reducer.py
  -mapper mapper.py \
  -reducer reducer.py \
  -input /mapreduce/test.txt \
  -output /mapreduce/output