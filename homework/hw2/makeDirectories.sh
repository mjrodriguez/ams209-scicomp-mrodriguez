#!/bin/bash

# This is a shell script to create 16 directories called exerciseXX

for i in {1..16}
do
	directoryName="exercise"
	n=$(printf %02s $i)
	directoryName=$directoryName$n
       	mkdir $directoryName
done  