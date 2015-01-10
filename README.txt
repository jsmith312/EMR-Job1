mapper1.py - This is the modified version of the wordSplitter.py program modified to parse the stdin as a json line of text and filters out the 'text' field of the json file. Also the regec was changed to include the characters '_-#@' as well as the alphabet and numbers to define one word. 

mapper2.py - counting words the words that start with either #, @ or just a regular word. Count results are put in a int dictionary object 

reducer.py - This was the aggregator.py. Almost no changes were made to this file. 

This was tested using the EMR GUI. For the first step the mapper is mapper1.py and the reducer.py is the reducer. the specified output of the results went into a folder in my s3 bucket and the input was grabbed from the final.json file from prof. Hartman's bucket. For the second step, the mapper2.py was used as the mapper and reducer for the EMR job. The input for this was the output from the previous job and the output went to a specified folder in my S3 bucket. 