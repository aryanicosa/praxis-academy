#!/bin/bash
echo "What's apps you want to stop?"
read app

app_pid=`ps -ef | grep -i $app | awk '{print $2}'`

if ps -p $app_pid > /dev/null; then
	echo "$app is Running";
	ps -p $app_pid;
	kill $app_pid;
fi
