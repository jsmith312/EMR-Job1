#!/usr/bin/python
import sys 
import re 
import fileinput
import json
import sys
import os
from collections import defaultdict

def main(argv): 
	line = []
	tw = 0
	# create the regex to satisfy the desired count for the 
	# tweets provided in the spec
	pattern = re.compile("[a-zA-Z0-9#@_-][a-zA-Z0-9#@_-]*") 
	# read in the line in stdin
	for line in sys.stdin: 
		# strip the line
		line = line.strip()
		if not line: 
			continue
		# parse the input as JSON and grab the 'text' object
		# from each line
		tweettext = json.loads(line).get('text')
		if not json.loads(line).get('text'):
			continue
		# print the lowered case word to stdout 
		for word in pattern.findall(tweettext): 
			print "LongValueSum:" + word.lower() + "\t" + "1"

if __name__ == "__main__": 
    main(sys.argv) 