#!/bin/bash

#changes to directory for ams209coursegit and cleans the build then rebuilds
PATH_2_COURSE=$ams209scicompgit

cd $PATH_2_COURSEl

#switches back to my ams209scicompgit repository
cd $ams209scicompgit/homework/hw1

#checks size of ams209coursegit directory and displays the first n lines.
du $PATH_2_COURSE | sort -nr | head -n 3 > output.txt && more output.txt
