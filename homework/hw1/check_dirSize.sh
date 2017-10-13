#!/bin/bash
du -a $ams209coursegit | sort -nr | head -3 > output.txt
