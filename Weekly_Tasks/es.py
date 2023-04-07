# This program reads in a text file and outputs the number of e's it contains
# It takes the filename from an argument on the command line
# Author: Tatjana Staunton

# created small txt file named data.txt
'''FILENAME = "data.txt" # defined FILENAME
with open (FILENAME, 'rt') as f: 
    for data in f:
        print(data) # read file and print out the content
        '''
filename = input("Please enter file name:") #asking user to input name of the file for program to read

with open (filename, 'rt') as f: 
    for data in f:
        print("The data in the file is: "+ data) # read file and print out the content