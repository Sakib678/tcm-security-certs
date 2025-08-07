#!/bin/bash

if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.176.42"

else
for ip in `seq 1 254`; do #for ip addresses from 1 to 254
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & 
done
fi


#Explanation of commands
#grep searches for a pattern and matches it to a given one
#the cut command extracts specific sections of data
#the tr command uses the "-d" option to delete characters from the given input
# the "$1" stands for the first argument that is given when the script is to be given

# the '&' allows the loop to run quicker
