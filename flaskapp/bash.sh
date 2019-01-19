#!/bin/sh


#the statement below puts the temp from ming and puts it into lov.
#it is form the lov that we will feed the flask app with

#similar implementation can be done for the other columns and the other sensors

while true;do
    echo "Reading Temp"
    tail -12 collector.txt | awk '{printf $4 " \t"  $6 " \n"}' > reading.embs
    sleep 60
done
