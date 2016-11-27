#!/bin/bash

if [ -e "fe" ]
then
	rm -f "fe"
fi
if [ -e "fee" ]
then
	rm -f "fee"
fi
if [ -e "be_process" ]
then
	rm -f "be_process"
fi
mkfifo fee

echo "flag=1" >>be_process
echo "while [ \$flag -eq 1 ] " >>be_process
echo "do" >>be_process
echo "read line <fee" >>be_process
echo "echo \$line" >>be_process
echo "if [ \"\$line\" == \"end_of_fifo\" ]" >>be_process
echo "then" >>be_process
echo "exit" >>be_process
echo "fi" >>be_process
echo "done" >>be_process

chmod u+x be_process
./be_process&

ls -la | awk '{print $0}' | while read line
do
	echo $line >>fe
	echo $line >>fee
done

echo "end_of_fifo" >>fee
#while read line
#do
#	echo $line
#done <fe
