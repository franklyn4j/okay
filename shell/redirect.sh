#!/bin/bash

if [ -e "fe" ]
then
	rm -f "fe"
fi
touch fe

ls -la | awk '{print $0}' | while read line
do
	echo $line >>fe
	echo $line >>fe
done

while read line
do
	echo $line
done <fe
