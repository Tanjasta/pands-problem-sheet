# This program reads in a text file and outputs the number of e's it contains
# It takes the filename from an argument on the command line
# Author: Tatjana Staunton

# created small txt file named data.txt
FILENAME = "data.txt" # defined FILENAME
with open (FILENAME, 'rt') as f:
    for data in f:
        print(data)
    
