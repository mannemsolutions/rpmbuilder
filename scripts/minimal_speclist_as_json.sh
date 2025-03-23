#!/bin/bash
echo -n "myspecs="
{
	echo "{"
	echo "\"arch\":[\"amd64\"],"
	echo "\"baseimage\":["
	i=0
	for img in rockylinux:9; do
		i+=1
		if [ "$i" -gt "1" ]; then
			echo -n ","
			echo
		fi
		echo -n "\"${img}\""
	done
	echo "],"
	echo "\"spec\":["
	i=0
	for spec in specs/*; do
		i+=1
		if [ "$i" -gt "1" ]; then
			echo -n ","
			echo
		fi
		echo -n "\"${spec}\""
	done
	echo
	echo "]}"
} | jq -c
