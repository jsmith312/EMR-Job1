#!/usr/bin/python
import sys 

# Inserts the item into its proper place in the list of top words
# An item is a (word, count) tuple.
def Insert(l, item):
    index = 0
    for (word, count) in l:
        if item[1] > count:
            break
        index += 1
    l.insert(index, item)

# List of top-ten (word, count) tuples. This is kept in sorted
# order with the highest count first.
topWords = []
topAnd = []
topHashTag = []

def main(argv): 
    # read the line in stdin
    for line in sys.stdin:
        (word, count) = line.split()
        count = int(count)
        if (len(word) >= 2):
            # check for the first letter in the word to 
            # see if it is a tweet or reference to another user
            if (word[0] != '@'):
                if (word[0] != '#'):
                    # If there are fewer than 10 items in the top-ten list
                    # or the count of the current word is greater than the
                    # last word on the list, then insert it into the list.
                    if (len(topWords) < 10) or (count > topWords[-1][1]):
                        Insert(topWords, (word, count))
                        # If there are now more than 10 items in the list then
                        # delete the last item.
                        if len(topWords) > 10:
                            topWords.pop()
            # check the first letter to see if is and '@' character  
            if (word[0] == '@'):
                if (len(topAnd) < 10) or (count > topAnd[-1][1]):
                        Insert(topAnd, (word, count))
                        # If there are now more than 10 items in the list then
                        # delete the last item.
                        if len(topAnd) > 10:
                            topAnd.pop()
            # check the first letter in the word and see if it is a hashtag
            if (word[0] == '#'):
                if (len(topHashTag) < 10) or (count > topHashTag[-1][1]):
                        Insert(topHashTag, (word, count))
                        # If there are now more than 10 items in the list then
                        # delete the last item.
                        if len(topHashTag) > 10:
                            topHashTag.pop()                                
    # Print the top-ten list.
    for (word, count) in topWords:
        print "%s\t%d" % (word, count)
    # Print the top-ten list.
    for (word, count) in topAnd:
        print "%s\t%d" % (word, count)
    # Print the top-ten list.    
    for (word, count) in topHashTag:
        print "%s\t%d" % (word, count)    

if __name__ == "__main__": 
    main(sys.argv) 