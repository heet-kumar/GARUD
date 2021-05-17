#!/bin/sh
#path="C:/Users/ABHIJEET/Desktop/test/" # Replace this with the path to your git repository. To get path, run pwd in the directory or right click and select properties of the folder  
path=$1
while true 
do
	inotifywait --recursive -qq -e attrib,create,delete,modify,delete_self,move,move_self,close_write $path
	echo "$path"   
    cd $path                              #> /dev/null &> /dev/null
	git pull                              #> /dev/null &> /dev/null
	git add --all                         #> /dev/null &> /dev/null
	now=$(date)                           #> /dev/null &> /dev/null
	git commit -m "Auto-Commit at : $now" #> /dev/null &> /dev/null	
	git push -u origin master             #> /dev/null &> /dev/null
    sleep 2
done