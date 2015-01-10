#!/usr/bin/python

import sys
import re
from collections import defaultdict


def main(argv):
	# create a dictionary to hold the count of each word
    counts = defaultdict(int)
   	# read the line in stdin
    for line in sys.stdin:
    	# check to see whether the line starts with 
    	# the string LongValueSum
        if line.startswith('LongValueSum'):
            (dummy, word, count) = re.split('[ \t:]', line)
            counts[word] += int(count)
    # sort the keys in the counts dictionary object
    for word in sorted(counts.keys()):
    	# print the word followed by the count 
    	# separated by a tab
        print "%s\t%d" % (word, counts[word])

if __name__ == "__main__": 
    main(sys.argv) 