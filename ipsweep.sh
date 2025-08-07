#!/bin/bash

for ip in `seq 1 254 : do #for ip addresses from 1 to 254
ping -c 192.168.197.$ip| grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & 
done
./ipsweep


#!#Explanation of commands
#grep searches for a pattern and matches it to a given one
#the cut command extracts specific sections of data
#the tr command uses the "-d" option to delete characters from the given input
